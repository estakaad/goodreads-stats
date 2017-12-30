import stats
import getbooks
import re
from tabulate import tabulate
import prettytable
import charts

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
            years = [int(x) for x in input('\nEnter the years you want to analyze separated by spaces.\n').split()]
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
    days = []
    x.align = 'l'
    for year in years:
        books = stats.bookReadForTheLongestInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([books_list[1], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
        days.append(books_list[1])
    print(x)
    charts.longestReadBooks(days, years)


def displayTotalPages(years, id):
    x = prettytable.PrettyTable(['Pages', 'Year'])
    x.align = 'l'
    count = []
    for year in years:
        pages = stats.totalPagesReadGivenYear(getbooks.getBooksFromShelfGivenYear(year, id))
        x.add_row([pages, year])
        count.append(int(pages))
    print(x)
    charts.totalPagesRead(count, years)


def displayAveragePagesPerDay(years, id):
    x = prettytable.PrettyTable(['Pages per day', 'Year'])
    count = []
    x.align = 'l'
    for year in years:
        pages = stats.averageNumberOfPagesReadInDay(getbooks.getBooksFromShelfGivenYear(year, id), year)
        x.add_row(['{0:.2f}'.format(pages), year])
        count.append(pages)
    print(x)
    charts.averageNumberOfPages(count, years)


def displayMostPopularBooks(years, id):
    x = prettytable.PrettyTable(['Number of ratings', 'Title', 'Author', 'Started', 'Finished'])
    count = []
    x.align = 'l'
    for year in years:
        books = stats.bookWithMostRatingsInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[4], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
        count.append(int(innerlist[4]))
    print(x)
    charts.mostPopularBooks(count, years)


def displayLeastPopularBooks(years, id):
    x = prettytable.PrettyTable(['Number of ratings', 'Title', 'Author', 'Started', 'Finished'])
    count = []
    x.align = 'l'
    for year in years:
        books = stats.bookWithLeastRatingsInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[4], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
        count.append(int(innerlist[4]))
    print(x)
    charts.leastPopularBooks(count, years)


def displayAverageNumberOfRatings(years, id):
    x = prettytable.PrettyTable(['Average ratings count', 'Year'])
    count = []
    x.align = 'l'
    for year in years:
        ratings = stats.averageNumberOfRatings(getbooks.getBooksFromShelfGivenYear(year, id))
        x.add_row(['{0:.2f}'.format(ratings), year])
        count.append(ratings)
    print(x)
    charts.averageNumberOfRatings(count, years)


def displayWorstBooks(years, id):
    x = prettytable.PrettyTable(['Rating', 'Title', 'Author', 'Started', 'Finished'])
    ratings = []
    x.align = 'l'
    for year in years:
        books = stats.worstBookRead(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[3], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
        ratings.append(float(innerlist[3]))
    print(x)
    charts.worstBooks(ratings, years)


def displayBestBooks(years, id):
    x = prettytable.PrettyTable(['Rating', 'Title', 'Author', 'Started', 'Finished'])
    ratings = []
    #titles = []
    x.align = 'l'
    bestBooks = [['Rating', 'Title', 'Author', 'Started', 'Finished']]
    for year in years:
        books = stats.bestBookRead(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[3], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
        ratings.append(float(innerlist[3]))
        #titles.append(innerlist[0])
    print(x)
    charts.bestBooks(ratings, years)


def displayAverageRating(years, id):
    x = prettytable.PrettyTable(['Average rating', 'Year'])
    ratings = []
    x.align = 'l'
    averageRating = [['Average rating', 'Year']]
    for year in years:
        averageRating = stats.averageRatingOfBook(getbooks.getBooksFromShelfGivenYear(year, id))
        x.add_row(['{0:.2f}'.format(averageRating), year])
        ratings.append(float(averageRating))
    print(x)
    charts.averageRating(ratings, years)
