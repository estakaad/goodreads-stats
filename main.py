import stats
import getbooks
import view


id = view.askForId()
years = view.askForYears()
fromFile = view.askLoadingFromFile()
view.displayQuestions()
q = ''

while q != 'q':
    q = input('Choose a question and enter the letter in front of it or enter q to quit.\n').lower()

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
        view.displayAllStats(years, id, fromFile)
    elif q == 'q':
        break
    else:
        print('You should\'ve followed the instructions.')
