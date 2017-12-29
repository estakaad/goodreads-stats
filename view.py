import stats
import getbooks
import re
from tabulate import tabulate
import prettytable

def askForId():
    regex = r'^\d+$'

    while True:
        try:
            id = str(input("\nPlease enter Goodread\'s user ID\n "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if re.search(regex, id):
          break
        else:
          print('Goodread\'s user ID must only contain non negative numbers.\n')
          continue

    return id


def askForYears():

    while True:
        try:
            years = [int(x) for x in input('\nEnter the years you want to analyze separated with spaces.\n').split()]
            break
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
    return years


def displayQuestions():

    table = [
             ['a', 'Which book took the longest to read?'],
             ['b', 'How many pages did I read in year x?'],
             ['c', 'How many pages did I read on an average day in year x?'],
             ['d', 'Which was the most popular book I read in year x?'],
             ['e', 'Which was the least popular book I read in year x?'],
             ['f', 'How popular was an average book I read in year x?'],
             ['g', 'What was the worst book I read in year x?'],
             ['h', 'What was the best book I read in year x?'],
             ['i', 'How good was the average book I read in year x?'],
            ]

    print(tabulate(table))


def displayLongestReadBooks(years, id):
    x = prettytable.PrettyTable(['Days read', 'Title', 'Author', 'Started', 'Finished'])
    x.align = 'l'
    for year in years:
        books = stats.bookReadForTheLongestInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([books_list[1], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
    print(x)


def displayTotalPages(years, id):
    x = prettytable.PrettyTable(['Pages', 'Year'])
    x.align = 'l'
    for year in years:
        pages = stats.totalPagesReadGivenYear(getbooks.getBooksFromShelfGivenYear(year, id))
        x.add_row([pages, year])
    print(x)


def displayAveragePagesPerDay(years, id):
    x = prettytable.PrettyTable(['Pages per day', 'Year'])
    x.align = 'l'
    for year in years:
        pages = stats.averageNumberOfPagesReadInDay(getbooks.getBooksFromShelfGivenYear(year, id), year)
        x.add_row(['{0:.2f}'.format(pages), year])
    print(x)


def displayMostPopularBooks(years, id):
    x = prettytable.PrettyTable(['Number of ratings', 'Title', 'Author', 'Started', 'Finished'])
    x.align = 'l'
    for year in years:
        books = stats.bookWithMostRatingsInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[4], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
    print(x)


def displayLeastPopularBooks(years, id):
    x = prettytable.PrettyTable(['Number of ratings', 'Title', 'Author', 'Started', 'Finished'])
    x.align = 'l'
    for year in years:
        books = stats.bookWithLeastRatingsInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[4], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
    print(x)


def displayAverageNumberOfRatings(years, id):
    x = prettytable.PrettyTable(['Average ratings count', 'Year'])
    x.align = 'l'
    for year in years:
        pages = stats.averageNumberOfRatings(getbooks.getBooksFromShelfGivenYear(year, id))
        x.add_row(['{0:.2f}'.format(pages), year])
    print(x)


def displayWorstBooks(years, id):
    x = prettytable.PrettyTable(['Rating', 'Title', 'Author', 'Started', 'Finished'])
    x.align = 'l'
    for year in years:
        books = stats.worstBookRead(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[3], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
    print(x)


def displayBestBooks(years, id):
    x = prettytable.PrettyTable(['Rating', 'Title', 'Author', 'Started', 'Finished'])
    x.align = 'l'
    bestBooks = [['Rating', 'Title', 'Author', 'Started', 'Finished']]
    for year in years:
        books = stats.bestBookRead(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[3], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
    print(x)


def displayAverageRating(years, id):
    x = prettytable.PrettyTable(['Average rating', 'Year'])
    x.align = 'l'
    averageRating = [['Average rating', 'Year']]
    for year in years:
        pages = stats.averageRatingOfBook(getbooks.getBooksFromShelfGivenYear(year, id))
        x.add_row(['{0:.2f}'.format(pages), year])
    print(x)
