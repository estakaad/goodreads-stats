import configparser
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import os
import json
from config import API_KEY


# A GET request to retrieve books on a user's shelf's one page. Returns a XML. API_KEY is a variable in config.py
def get_books_on_page(user_id, page):

    key = API_KEY
    v = '2'
    shelf = 'read'
    per_page = '50'

    r = requests.get('https://www.goodreads.com/review/list/'
        + str(user_id)
        + '.xml?key='
        + key
        + '&v='
        + v
        + '&id='
        + str(user_id)
        + '&shelf='
        + shelf
        + '&page='
        + str(page)
        + '&per_page='
        + per_page)

    return ET.fromstring(r.content)


# GET request to get user info
def get_user_info(user_id):

    r = requests.get('https://www.goodreads.com/user/show/' + str(user_id) + '.xml?key=' + API_KEY)

    return ET.fromstring(r.content)


# Returns a dictionary of all the books on a user's Goodreads read-shelf.
def get_all_books_on_shelf(user_id):

    r = get_user_info(user_id)
    user_name = r[1][1].text

    books = {}
    nth_book_on_page = 0
    page = 1

    number_of_books_on_page = len(list(get_books_on_page(user_id, page).iter('review')))

    while nth_book_on_page < number_of_books_on_page:
        number_of_books_on_page = len(list(get_books_on_page(user_id, page).iter('review')))
        for review in get_books_on_page(user_id, page).iter('review'):
            nth_book_on_page+=1
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

            if user_name is None:
                books[review[0].text]['username'] = ''
            else:
                books[review[0].text]['username'] = user_name

            if nth_book_on_page != number_of_books_on_page:
                continue
            else:
                nth_book_on_page = 0
                page += 1

    return books


# Saves dictionary to file
def serialize_books(books, user_id):
    file_name = 'books/' + str(user_id) + '.json'
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    with open(file_name, 'w') as out_file:
        json.dump(books, out_file, indent=4)
    out_file.close()


# Reads dictionary from file
def deserialize_books(file):
    with open(file) as json_file:
        dictionary = json.load(json_file)
    return dictionary


# Returns all books the user has marked as read. This can be done either making
# a GET request or loading the file with the serialized dictionary. In case
# loading from file is chosen, a file with a user's Goodreads' ID is looked for.
# In case it doesn't exist, a GET request is made instead. After a GET request,
# the results are serialized.
def load_from_file_or_fetch_new_data_and_serialize(user_id, from_file):
    filename = 'books/' + str(user_id) + '.json'

    if from_file:
        try:
            books = deserialize_books(filename)
        except IOError:
            print('File does not appear to exist. Trying get books from Goodreads instead...')
            books = get_all_books_on_shelf(user_id)
            serialize_books(books, user_id)
    else:
        books = get_all_books_on_shelf(user_id)
        serialize_books(books, user_id)

    return books


# Returns a dictionary of books finished during the given year.
def get_books_from_shelf_given_year(year, user_id, from_file):
    books_in_year = load_from_file_or_fetch_new_data_and_serialize(user_id, from_file)

    books_in_year = {k: v for k, v in books_in_year.items() if v['read_at'] != '-'}
    books_in_year = {k: v for k, v in books_in_year.items() if datetime.strptime(str(v['read_at']), '%a %b %d %H:%M:%S %z %Y').year == year}

    return books_in_year
