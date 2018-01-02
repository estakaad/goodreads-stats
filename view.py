import stats
import getbooks
import re
import prettytable
import charts

allUsersValues = []
allUserNames = []

def askForId():

    while True:
        try:
            ids = [int(x) for x in input('\nEnter Goodreads\' users\' ID\'s separated by spaces.\n').split()]
            break
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
    return ids


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


def addUserNameAndOtherValuesToList(userNames, count, userCount, years, createChart):

    for userName in userNames:
        if userName == '':
            userNames.remove(userName)
    userNames = list(set(userNames))

    allUsersValues.append(count)
    allUserNames.append(userNames)

    if len(allUsersValues) == userCount:
        createChart(allUsersValues, years, allUserNames)
        allUsersValues.clear()
        allUserNames.clear()


def displayLongestReadBooks(years, id, fromFile, userCount):

    x = prettytable.PrettyTable(['Days read', 'Title', 'Author', 'Started', 'Finished'])
    days = []
    titles = []
    x.align = 'l'

    for year in years:
        books = stats.bookReadForTheLongestInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        if len(books) != 0:
            books_list = list(books.values())
            innerlist = list(books_list[0].values())
            x.add_row([books_list[1], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
            days.append(books_list[1])
            titles.append(innerlist[0])
        else:
            x.add_row(['-', '-', '-', '-', '-'])
            days.append(0)
            titles.append('-')

    allUsersValues.append(days)

    print('BOOKS THAT TOOK THE LONGEST TO FINISH')
    print(x)

    if len(allUsersValues) == userCount:
        charts.longestReadBooks(allUsersValues, years)
        allUsersValues.clear()


def displayTotalPages(years, id, fromFile, userCount):

    x = prettytable.PrettyTable(['Pages', 'Year'])
    x.align = 'l'
    count = []
    userNames = []
    for year in years:
        usersPages = stats.totalPagesReadGivenYear(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        x.add_row([usersPages[0], year])
        count.append(int(usersPages[0]))
        userNames.append(usersPages[1])

    print('TOTAL NUMBER OF PAGES READ')
    print(x)

    addUserNameAndOtherValuesToList(userNames, count, userCount, years, charts.totalPagesRead)


def displayAveragePagesPerDay(years, id, fromFile, userCount):

    x = prettytable.PrettyTable(['Pages per day', 'Year'])
    count = []
    x.align = 'l'
    for year in years:
        pages = stats.averageNumberOfPagesReadInDay(getbooks.getBooksFromShelfGivenYear(year, id, fromFile), year)
        x.add_row(['{0:.2f}'.format(pages), year])
        count.append(pages)

    allUsersValues.append(count)

    print('AVERAGE NUMBER OF PAGES READ PER DAY')
    print(x)

    if len(allUsersValues) == userCount:
        charts.averageNumberOfPages(allUsersValues, years)
        allUsersValues.clear()


def displayMostPopularBooks(years, id, fromFile, userCount):

    x = prettytable.PrettyTable(['Number of ratings', 'Title', 'Author', 'Started', 'Finished'])
    count = []
    titles = []
    userNames = []
    x.align = 'l'
    for year in years:
        books = stats.bookWithMostRatingsInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        if len(books) != 0:
            books_list = list(books.values())
            innerlist = list(books_list[0].values())
            x.add_row([innerlist[4], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
            count.append(int(innerlist[4]))
            titles.append(innerlist[0])
        else:
            x.add_row(['-', '-', '-', '-', '-'])
            count.append(0)
            titles.append('-')

    allUsersValues.append(count)
    allUserNames.append(innerlist[7])

    print('MOST POPULAR BOOKS READ (POPULAR = BOOKS WITH THE HIGHEST NUMBER OF RATINGS)')
    print(x)

    if len(allUsersValues) == userCount:
        charts.mostPopularBooks(allUsersValues, years, allUserNames)
        allUsersValues.clear()
        allUserNames.clear()


def displayLeastPopularBooks(years, id, fromFile, userCount):

    x = prettytable.PrettyTable(['Number of ratings', 'Title', 'Author', 'Started', 'Finished'])
    count = []
    titles = []
    usernames = []
    x.align = 'l'
    for year in years:
        books = stats.bookWithLeastRatingsInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        if len(books) != 0:
            books_list = list(books.values())
            innerlist = list(books_list[0].values())
            x.add_row([innerlist[4], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
            count.append(int(innerlist[4]))
            titles.append(innerlist[0])
        else:
            x.add_row(['-', '-', '-', '-', '-'])
            count.append(0)
            titles.append('-')

    allUsersValues.append(count)
    allUserNames.append(innerlist[7])

    print('LEAST POPULAR BOOKS READ (LEAST POPULAR = BOOKS WITH THE LOWEST NUMBER OF RATINGS)')
    print(x)

    if len(allUsersValues) == userCount:
        charts.leastPopularBooks(allUsersValues, years, allUserNames)
        allUsersValues.clear()
        allUserNames.clear()


def displayAverageNumberOfRatings(years, id, fromFile, userCount):

    x = prettytable.PrettyTable(['Average ratings count', 'Year'])
    count = []
    #usernames = []
    x.align = 'l'
    for year in years:
        ratings = stats.averageNumberOfRatings(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        x.add_row(['{0:.2f}'.format(ratings), year])
        count.append(ratings)

    allUsersValues.append(count)
    #allUserNames.append()

    print('AVERAGE NUMBER OF RATINGS OF BOOKS READ')
    print(x)

    if len(allUsersValues) == userCount:
        charts.averageNumberOfRatings(allUsersValues, years)
        allUsersValues.clear()


def displayWorstBooks(years, id, fromFile, userCount):

    x = prettytable.PrettyTable(['Rating', 'Title', 'Author', 'Started', 'Finished'])
    ratings = []
    titles = []
    userNames = []
    x.align = 'l'
    for year in years:
        books = stats.worstBookRead(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        if len(books) != 0:
            books_list = list(books.values())
            innerlist = list(books_list[0].values())
            x.add_row([innerlist[3], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
            ratings.append(float(innerlist[3]))
            titles.append(innerlist[0])
        else:
            x.add_row(['-', '-', '-', '-', '-'])
            ratings.append(0)
            titles.append('-')
        userNames.append(innerlist[7])

    print('WORST BOOKS READ')
    print(x)

    addUserNameAndOtherValuesToList(userNames, ratings, userCount, years, charts.worstBooks)


def displayBestBooks(years, id, fromFile, userCount):

    x = prettytable.PrettyTable(['Rating', 'Title', 'Author', 'Started', 'Finished'])
    ratings = []
    titles = []
    userNames = []
    x.align = 'l'
    for year in years:
        books = stats.bestBookRead(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        if len(books) != 0:
            books_list = list(books.values())
            innerlist = list(books_list[0].values())
            x.add_row([innerlist[3], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
            ratings.append(float(innerlist[3]))
            titles.append(innerlist[0])
        else:
            x.add_row(['-', '-', '-', '-', '-'])
            ratings.append(0)
            titles.append('-')
        userNames.append(innerlist[7])

    print('BEST BOOKS READ')
    print(x)

    addUserNameAndOtherValuesToList(userNames, ratings, userCount, years, charts.bestBooks)


def displayAverageRating(years, id, fromFile, userCount):

    x = prettytable.PrettyTable(['Average rating', 'Year'])
    ratings = []
    x.align = 'l'
    averageRating = [['Average rating', 'Year']]
    for year in years:
        averageRating = stats.averageRatingOfBook(getbooks.getBooksFromShelfGivenYear(year, id, fromFile))
        x.add_row(['{0:.2f}'.format(averageRating), year])
        ratings.append(float(averageRating))

    allUsersValues.append(ratings)

    print('AVERAGE RATING OF BOOKS READ')
    print(x)

    if len(allUsersValues) == userCount:
        charts.averageRating(allUsersValues, years)
        allUsersValues.clear()

