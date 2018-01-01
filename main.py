import stats
import getbooks
import view


ids = view.askForId()
years = view.askForYears()
fromFile = view.askLoadingFromFile()
view.displayQuestions()
q = ''

while q != 'q':

    q = input().lower()

    if q == 'a':
        for id in ids:
            view.displayLongestReadBooks(years, id, fromFile)
    elif q == 'b':
        for id in ids:
            view.displayTotalPages(years, id, fromFile)
    elif q == 'c':
        for id in ids:
            view.displayAveragePagesPerDay(years, id, fromFile)
    elif q == 'd':
        for id in ids:
            view.displayMostPopularBooks(years, id, fromFile)
    elif q == 'e':
        for id in ids:
            view.displayLeastPopularBooks(years, id, fromFile)
    elif q == 'f':
        for id in ids:
            view.displayAverageNumberOfRatings(years, id, fromFile)
    elif q == 'g':
        for id in ids:
            view.displayWorstBooks(years, id, fromFile)
    elif q == 'h':
        for id in ids:
            view.displayBestBooks(years, id, fromFile)
    elif q == 'i':
        for id in ids:
            view.displayAverageRating(years, id, fromFile)
    elif q == 'j':
        for id in ids:
            view.displayLongestReadBooks(years, id, fromFile)
            view.displayTotalPages(years, id, fromFile)
            view.displayAveragePagesPerDay(years, id, fromFile)
            view.displayMostPopularBooks(years, id, fromFile)
            view.displayLeastPopularBooks(years, id, fromFile)
            view.displayAverageNumberOfRatings(years, id, fromFile)
            view.displayWorstBooks(years, id, fromFile)
            view.displayBestBooks(years, id, fromFile)
            view.displayAverageRating(years, id, fromFile)
    elif q == 'q':
        break
    else:
        print('You should\'ve followed the instructions.')
