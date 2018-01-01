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
            view.displayLongestReadBooks(years, id, fromFile, len(ids))
    elif q == 'b':
        for id in ids:
            view.displayTotalPages(years, id, fromFile, len(ids))
    elif q == 'c':
        for id in ids:
            view.displayAveragePagesPerDay(years, id, fromFile, len(ids))
    elif q == 'd':
        for id in ids:
            view.displayMostPopularBooks(years, id, fromFile, len(ids))
    elif q == 'e':
        for id in ids:
            view.displayLeastPopularBooks(years, id, fromFile, len(ids))
    elif q == 'f':
        for id in ids:
            view.displayAverageNumberOfRatings(years, id, fromFile, len(ids))
    elif q == 'g':
        for id in ids:
            view.displayWorstBooks(years, id, fromFile, len(ids))
    elif q == 'h':
        for id in ids:
            view.displayBestBooks(years, id, fromFile, len(ids))
    elif q == 'i':
        for id in ids:
            view.displayAverageRating(years, id, fromFile, len(ids))
    elif q == 'j':
        for id in ids:
            view.displayLongestReadBooks(years, id, fromFile, len(ids))
            view.displayTotalPages(years, id, fromFile, len(ids))
            view.displayAveragePagesPerDay(years, id, fromFile, len(ids))
            view.displayMostPopularBooks(years, id, fromFile, len(ids))
            view.displayLeastPopularBooks(years, id, fromFile, len(ids))
            view.displayAverageNumberOfRatings(years, id, fromFile, len(ids))
            view.displayWorstBooks(years, id, fromFile, len(ids))
            view.displayBestBooks(years, id, fromFile, len(ids))
            view.displayAverageRating(years, id, fromFile, len(ids))
    elif q == 'q':
        break
    else:
        print('You should\'ve followed the instructions.')
