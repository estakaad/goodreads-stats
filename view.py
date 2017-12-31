import stats
import getbooks
import re
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

    print('Choose a question and enter the letter in front of it or enter q to quit.\n')

    table = prettytable.PrettyTable(['Option', 'Question'])

    questions = [
                 ['a', 'Which book took the longest to read?'],
                 ['b', 'How many pages did I read in year x?'],
                 ['c', 'How many pages did I read on an average day in year x?'],
                 ['d', 'Which was the most popular book I read in year x?'],
                 ['e', 'Which was the least popular book I read in year x?'],
                 ['f', 'How popular was an average book I read in year x?'],
                 ['g', 'What was the worst book I read in year x?'],
                 ['h', 'What was the best book I read in year x?'],
                 ['i', 'How good was the average book I read in year x?'],
                 ['j', 'Show me all the answers!']
                ]

    for question in questions:
        table.add_row(question)

    table.align = 'l'
    print(table)


def askLoadingFromFile():

    option = input('Do you want to load the books from a file? y/n \n')

    if option == 'y':
        return True

    return False


def getDataForChart():
    return


def displayLongestReadBooks(years, id, fromFile):
    x = prettytable.PrettyTable(['Days read', 'Title', 'Author', 'Started', 'Finished'])
    days = []
    titles = []
    x.align = 'l'
    for year in years:
        books = stats.bookReadForTheLongestInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([books_list[1], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
        days.append(books_list[1])
        titles.append(innerlist[0])
    print('')
    print('BOOKS THAT TOOK THE LONGEST TO FINISH')
    print(x)
    charts.longestReadBooks(days, years, titles)


def displayTotalPages(years, id, fromFile):
    x = prettytable.PrettyTable(['Pages', 'Year'])
    x.align = 'l'
    count = []
    for year in years:
        pages = stats.totalPagesReadGivenYear(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        x.add_row([pages, year])
        count.append(int(pages))
    print('')
    print('TOTAL NUMBER OF PAGES READ')
    print(x)
    charts.totalPagesRead(count, years)


def displayAveragePagesPerDay(years, id, fromFile):
    x = prettytable.PrettyTable(['Pages per day', 'Year'])
    count = []
    x.align = 'l'
    for year in years:
        pages = stats.averageNumberOfPagesReadInDay(getbooks.getBooksFromShelfGivenYear(year, id, fromFile), year)
        x.add_row(['{0:.2f}'.format(pages), year])
        count.append(pages)
    print('')
    print('AVERAGE NUMBER OF PAGES READ PER DAY')
    print(x)
    charts.averageNumberOfPages(count, years)


def displayMostPopularBooks(years, id, fromFile):
    x = prettytable.PrettyTable(['Number of ratings', 'Title', 'Author', 'Started', 'Finished'])
    count = []
    titles = []
    x.align = 'l'
    for year in years:
        books = stats.bookWithMostRatingsInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[4], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
        count.append(int(innerlist[4]))
        titles.append(innerlist[0])
    print('')
    print('MOST POPULAR BOOKS READ (POPULAR = BOOKS WITH THE HIGHEST NUMBER OF RATINGS)')
    print(x)
    charts.mostPopularBooks(count, years, titles)


def displayLeastPopularBooks(years, id, fromFile):
    x = prettytable.PrettyTable(['Number of ratings', 'Title', 'Author', 'Started', 'Finished'])
    count = []
    titles = []
    x.align = 'l'
    for year in years:
        books = stats.bookWithLeastRatingsInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[4], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
        count.append(int(innerlist[4]))
        titles.append(innerlist[0])
    print('')
    print('LEAST POPULAR BOOKS READ (LEAST POPULAR = BOOKS WITH THE LOWEST NUMBER OF RATINGS)')
    print(x)
    charts.leastPopularBooks(count, years, titles)


def displayAverageNumberOfRatings(years, id, fromFile):
    x = prettytable.PrettyTable(['Average ratings count', 'Year'])
    count = []
    x.align = 'l'
    for year in years:
        ratings = stats.averageNumberOfRatings(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        x.add_row(['{0:.2f}'.format(ratings), year])
        count.append(ratings)
    print('')
    print('AVERAGE NUMBER OF RATINGS OF BOOKS READ')
    print(x)
    charts.averageNumberOfRatings(count, years)


def displayWorstBooks(years, id, fromFile):
    x = prettytable.PrettyTable(['Rating', 'Title', 'Author', 'Started', 'Finished'])
    ratings = []
    titles = []
    x.align = 'l'
    for year in years:
        books = stats.worstBookRead(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[3], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
        ratings.append(float(innerlist[3]))
        titles.append(innerlist[0])
    print('')
    print('WORST BOOKS READ')
    print(x)
    charts.worstBooks(ratings, years, titles)


def displayBestBooks(years, id, fromFile):
    x = prettytable.PrettyTable(['Rating', 'Title', 'Author', 'Started', 'Finished'])
    ratings = []
    titles = []
    x.align = 'l'
    for year in years:
        books = stats.bestBookRead(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        x.add_row([innerlist[3], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
        ratings.append(float(innerlist[3]))
        titles.append(innerlist[0])
    print('')
    print('BEST BOOKS READ')
    print(x)
    charts.bestBooks(ratings, years, titles)


def displayAverageRating(years, id, fromFile):
    x = prettytable.PrettyTable(['Average rating', 'Year'])
    ratings = []
    x.align = 'l'
    averageRating = [['Average rating', 'Year']]
    for year in years:
        averageRating = stats.averageRatingOfBook(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        x.add_row(['{0:.2f}'.format(averageRating), year])
        ratings.append(float(averageRating))
    print('')
    print('AVERAGE RATING OF BOOKS READ')
    print(x)
    charts.averageRating(ratings, years)
