import stats
import getbooks
import view


id = view.askForId()
years = view.askForYears()
view.displayQuestions()
q = ''

while q != 'q':
    q = input('Choose a question and enter the letter in front of it or enter q to quit.\n').lower()

    if q == 'a':
        view.displayLongestReadBooks(years, id)
    elif q == 'b':
        view.displayTotalPages(years, id)
    elif q == 'c':
        view.displayAveragePagesPerDay(years, id)
    elif q == 'd':
        view.displayMostPopularBooks(years, id)
    elif q == 'e':
        view.displayLeastPopularBooks(years, id)
    elif q == 'f':
        view.displayAverageNumberOfRatings(years, id)
    elif q == 'g':
        view.displayWorstBooks(years, id)
    elif q == 'h':
        view.displayBestBooks(years, id)
    elif q == 'i':
        view.displayAverageRating(years, id)
    elif q == 'q':
        break
    else:
        print('You should\'ve followed the instructions.')


#chart = input('Do you want to generate a chart based on the data? (y/n)\n').lower()

# if y:
#     print('create chart')
# else:
#     break
