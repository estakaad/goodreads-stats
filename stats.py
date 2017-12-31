from datetime import datetime
import sys
import re
import calendar
import getbooks


# Returns the book that took the longest to read in the given year. It doesn't
# necessarily mean that the user started reading the book the same year it
# was finished. If the date of starting a book or finishing it unknown,
# the book is skipped.
def bookReadForTheLongestInGivenYear(books):

    bookReadForTheLongest = {}
    numberOfDays = 0

    for key, value in books.items():
        if ((str(value['started_at']) != '-') and (str(value['read_at']) != '-')):
            dateStarted = datetime.strptime(str(value['started_at']), '%a %b %d %H:%M:%S %z %Y')
            dateFinished = datetime.strptime(str(value['read_at']), '%a %b %d %H:%M:%S %z %Y')
            delta = (dateFinished - dateStarted).days + 1

            if delta > numberOfDays:
                numberOfDays = delta
                bookReadForTheLongest = {key: value, 'numberOfDaysRead': numberOfDays}

    return bookReadForTheLongest


# Returns number of pages read in the given year
def totalPagesReadGivenYear(books):

    totalPagesPerYear = 0

    for key, value in books.items():
        if value['num_pages'] != '-':
            totalPagesPerYear+=int(value['num_pages'])

    return totalPagesPerYear


# Returns average number of pages read per day in the given year.
def averageNumberOfPagesReadInDay(books, year):

    if calendar.isleap(year):
        averagePagesPerDey = totalPagesReadGivenYear(books) / 366
    else:
        averagePagesPerDey = totalPagesReadGivenYear(books) / 365

    return averagePagesPerDey


# Returns the book with the most ratings among the books read in given year.
def bookWithMostRatingsInGivenYear(books):

    bookWithMostRatings = {}
    numberOfRatings = 0

    for key, value in books.items():
        if int(value['ratings_count']) > numberOfRatings:
            numberOfRatings = int(value['ratings_count'])
            bookWithMostRatings = {key: value}

    return bookWithMostRatings


# Returns the book with the least ratings among the books read in given year.
def bookWithLeastRatingsInGivenYear(books):

    bookWithLeastRatings = {}
    numberOfRatings = sys.maxsize

    for key, value in books.items():
        if int(value['ratings_count']) <= numberOfRatings:
            numberOfRatings = int(value['ratings_count'])
            bookWithLeastRatings = {key: value}

    return bookWithLeastRatings


# Returns the number of ratings a book read this year has on average.
def averageNumberOfRatings(books):

    sumOfCountOfRatings = 0
    numberOfRatings = 0

    for key, value in books.items():
        numberOfRatings+=1
        sumOfCountOfRatings += int(value['ratings_count'])

    # In case of zero ratings.
    while True:
        try:
            return sumOfCountOfRatings / numberOfRatings
            break
        except ZeroDivisionError:
            return 0


# Returns the worst book read in the given year. The worst meaning having
# the lowest average rating. Only takes into account books that have
# at least 15 ratings.
def worstBookRead(books):

    worstBook = {}
    worstRating = 5.00

    for key, value in books.items():
        if int(value['ratings_count']) >= 15:
            if float(value['average_rating']) <= worstRating:
                worstRating = float(value['average_rating'])
                worstBook = {key: value}

    return worstBook


# Returns the best book read in the given year. The best meaning having
# the lowest average rating. Only takes into account books that have
# at least 15 ratings.
def bestBookRead(books):

    bestBook = {}
    bestRating = 0.00

    for key, value in books.items():
        if int(value['ratings_count']) >= 15:
            if float(value['average_rating']) > bestRating:
                bestRating = float(value['average_rating'])
                bestBook = {key: value}

    return bestBook


# Returns an average rating of books read during the given year. Only takes
# into account books that have at least 15 ratings.
def averageRatingOfBook(books):

    numberOfRatings = 0
    sumOfRatings = 0

    for key, value in books.items():
        if int(value['ratings_count']) >= 15:
            sumOfRatings+=float(value['average_rating'])
            numberOfRatings+=1

    # In case of zero ratings.
    while True:
        try:
            return sumOfRatings / numberOfRatings
            break
        except ZeroDivisionError:
            return 0
