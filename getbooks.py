import configparser
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import pickle
import view
import os
import json

config = configparser.ConfigParser()
config.read("config.ini")


# Helper function for getting settings from config.ini
def configSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


# A GET request to retrieve books on a user's shelf's one page. Returns a XML.
def getBooksOnPage(userId, page):

    key = configSectionMap("SectionOne")['key']
    v = configSectionMap("SectionOne")['v']
    shelf = configSectionMap("SectionOne")['shelf']
    per_page = str(configSectionMap("SectionOne")['per_page'])

    r = requests.get('https://www.goodreads.com/review/list/' \
        + str(userId) \
        + '.xml?key=' \
        + key \
        + '&v=' \
        + v \
        + '&id=' \
        + str(userId) \
        + '&shelf=' \
        + shelf \
        + '&page=' \
        + str(page) \
        + '&per_page=' \
        + per_page)

    return ET.fromstring(r.content)


# Returns a dictionary of all the books on a user's Goodreads read-shelf.
def getAllBooksOnShelf(userId):

    books = {}
    nthBookOnPage = 0
    page = 1

    numberOfBooksOnPage = len(list(getBooksOnPage(userId, page).iter('review')))

    while nthBookOnPage < numberOfBooksOnPage:
        numberOfBooksOnPage = len(list(getBooksOnPage(userId, page).iter('review')))
        for review in getBooksOnPage(userId, page).iter('review'):
            nthBookOnPage+=1
            books[review[0].text] = {}

            if review[1][5].text is None:
                books[review[0].text]['title'] = '-'
            else:
                books[review[0].text]['title'] = review[1][5].text

            if review[1][21][0][1].text is None:
                books[review[0].text]['author'] = '-'
            else:
                books[review[0].text]['author'] = review[1][21][0][1].text

            if review[1][11].text is None:
                books[review[0].text]['num_pages'] = '-'
            else:
                books[review[0].text]['num_pages'] = review[1][11].text

            if review[1][18].text is None:
                books[review[0].text]['average_rating'] = '-'
            else:
                books[review[0].text]['average_rating'] = review[1][18].text

            if review[1][19].text is None:
                books[review[0].text]['ratings_count'] = '-'
            else:
                books[review[0].text]['ratings_count'] = review[1][19].text

            if review[9].text is None:
                books[review[0].text]['started_at'] = '-'
            else:
                books[review[0].text]['started_at'] = review[9].text

            if review[10].text is None:
                books[review[0].text]['read_at'] = '-'
            else:
                books[review[0].text]['read_at'] = review[10].text

            if nthBookOnPage != numberOfBooksOnPage:
                continue
            else:
                nthBookOnPage = 0
                page+=1

    return books


# Saves dictionary to file
def serializeBooks(books, userId):
    filename = 'books/'+ str(userId) + '.json'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as outfile:
        json.dump(books, outfile, indent=4)
    outfile.close()


# Reads dictionary from file
def deserializeBooks(file):
    with open(file) as json_file:
        dict = json.load(json_file)
    return dict


# Returns all books the user has marked as read. This can be done either making
# a GET request or loading the file with the serialized dictionary. In case
# loading from file is chosen, a file with a user's Goodread's ID is looked for.
# In case it doesn't exist, a GET request is made instead. After a GET request,
# the results are serialized.
def loadFromFileOrFetchNewDataAndSerialize(userId, fromFile):
    filename = 'books/'+ str(userId) + '.json'
    books = {}

    if fromFile:
        try:
            books = deserializeBooks(filename)
        except IOError:
            print('File does not appear to exist. Trying get books from Goodreads instead...')
            books = getAllBooksOnShelf(userId)
            serializeBooks(books, userId)
    else:
        books = getAllBooksOnShelf(userId)
        serializeBooks(books, userId)

    return books


# Returns a dictionary of books finished during the given year.
def getBooksFromShelfGivenYear(year, userId, fromFile):
    booksInYear = loadFromFileOrFetchNewDataAndSerialize(userId, fromFile)

    booksInYear = { k:v for k,v in booksInYear.items() if v['read_at'] != '-' }
    booksInYear = { k:v for k,v in booksInYear.items() if datetime.strptime(str(v['read_at']), '%a %b %d %H:%M:%S %z %Y').year == year }

    return booksInYear
