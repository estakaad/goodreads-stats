import stats
import getbooks
import view


id = view.askForId()
years = view.askForYears()
fromFile = view.askLoadingFromFile()
view.displayQuestions()
q = ''

while q != 'q':

    q = input().lower()

    if q == 'a':
        view.displayLongestReadBooks(years, id, fromFile)
    elif q == 'b':
        view.displayTotalPages(years, id, fromFile)
    elif q == 'c':
        view.displayAveragePagesPerDay(years, id, fromFile)
    elif q == 'd':
        view.displayMostPopularBooks(years, id, fromFile)
    elif q == 'e':
        view.displayLeastPopularBooks(years, id, fromFile)
    elif q == 'f':
        view.displayAverageNumberOfRatings(years, id, fromFile)
    elif q == 'g':
        view.displayWorstBooks(years, id, fromFile)
    elif q == 'h':
        view.displayBestBooks(years, id, fromFile)
    elif q == 'i':
        view.displayAverageRating(years, id, fromFile)
    elif q == 'j':
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
