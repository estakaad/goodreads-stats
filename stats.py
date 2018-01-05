from datetime import datetime
import sys
import calendar


# Returns the book that took the longest to read in the given year. It doesn't
# necessarily mean that the user started reading the book the same year it
# was finished. If the date of starting a book or finishing it unknown,
# the book is skipped.
def book_read_for_the_longest_in_given_year(books):

    book_read_for_the_longest = {}
    number_of_days = 0

    for key, value in books.items():
        if (str(value['started_at']) != '-') and (str(value['read_at']) != '-'):
            date_started = datetime.strptime(str(value['started_at']), '%a %b %d %H:%M:%S %z %Y')
            date_finished = datetime.strptime(str(value['read_at']), '%a %b %d %H:%M:%S %z %Y')
            delta = (date_finished - date_started).days + 1

            if delta > number_of_days:
                number_of_days = delta
                book_read_for_the_longest = {key: value, 'numberOfDaysRead': number_of_days}

    return book_read_for_the_longest


# Returns number of pages read in the given year
def total_pages_read_given_year(books):

    total_pages_per_year = 0
    user_name = ''
    users_pages = []

    for key, value in books.items():
        if value['num_pages'] != '-':
            total_pages_per_year += int(value['num_pages'])
        else:
            total_pages_per_year += 0
        user_name = value['username']

    users_pages.append(total_pages_per_year)
    users_pages.append(user_name)

    return users_pages


# Returns average number of pages read per day in the given year.
def average_number_of_pages_read_in_day(books, year):

    total_pages = total_pages_read_given_year(books)
    user_name = ''

    for key, value in books.items():
        user_name = value['username']

    average_pages_per_day = 0
    users_average_pages_per_day = []

    if calendar.isleap(year):
        average_pages_per_day = total_pages[0] / 366
    else:
        average_pages_per_day = total_pages[0] / 365

    users_average_pages_per_day.append(average_pages_per_day)
    users_average_pages_per_day.append(user_name)

    return users_average_pages_per_day


# Returns the book with the most ratings among the books read in given year.
def book_with_most_ratings_in_given_year(books):

    book_with_most_ratings = {}
    number_of_ratings = 0

    for key, value in books.items():
        if int(value['ratings_count']) > number_of_ratings:
            number_of_ratings = int(value['ratings_count'])
            book_with_most_ratings = {key: value}

    return book_with_most_ratings


# Returns the book with the least ratings among the books read in given year.
def book_with_least_ratings_in_given_year(books):

    book_with_least_ratings = {}
    number_of_ratings = sys.maxsize

    for key, value in books.items():
        if int(value['ratings_count']) <= number_of_ratings:
            number_of_ratings = int(value['ratings_count'])
            book_with_least_ratings = {key: value}

    return book_with_least_ratings


# Returns the number of ratings a book read this year has on average.
def average_number_of_ratings(books):

    sum_of_count_of_ratings = 0
    number_of_ratings = 0
    user_name = ''
    users_average_number_of_ratings = []

    for key, value in books.items():
        number_of_ratings+=1
        sum_of_count_of_ratings += int(value['ratings_count'])
        user_name = value['username']

    if number_of_ratings != 0:
        users_average_number_of_ratings.append(sum_of_count_of_ratings / number_of_ratings)
    else:
        users_average_number_of_ratings.append(0)

    users_average_number_of_ratings.append(user_name)

    return users_average_number_of_ratings


# Returns the worst book read in the given year. The worst meaning having
# the lowest average rating. Only takes into account books that have
# at least 15 ratings.
def worst_book_read(books):

    worst_book = {}
    worst_rating = 5.00

    for key, value in books.items():
        if int(value['ratings_count']) >= 15:
            if float(value['average_rating']) <= worst_rating:
                worst_rating = float(value['average_rating'])
                worst_book = {key: value}

    return worst_book


# Returns the best book read in the given year. The best meaning having
# the lowest average rating. Only takes into account books that have
# at least 15 ratings.
def best_book_read(books):

    best_book = {}
    best_rating = 0.00

    for key, value in books.items():
        if int(value['ratings_count']) >= 15:
            if float(value['average_rating']) > best_rating:
                best_rating = float(value['average_rating'])
                best_book = {key: value}

    return best_book


# Returns an average rating of books read during the given year. Only takes
# into account books that have at least 15 ratings.
def average_rating_of_book(books):

    number_of_ratings = 0
    sum_of_ratings = 0
    user_name = ''
    users_average_rating = []

    for key, value in books.items():
        if int(value['ratings_count']) >= 15:
            sum_of_ratings+=float(value['average_rating'])
            number_of_ratings+=1
        user_name = value['username']

    if number_of_ratings != 0:
        users_average_rating.append(sum_of_ratings / number_of_ratings)
    else:
        users_average_rating.append(0)

    users_average_rating.append(user_name)

    return users_average_rating
