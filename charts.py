import matplotlib.pyplot as plt
import stats
import getbooks
import view

# Draws the chart for longest read books

def chartLongestReadBooks():
    years = [2011, 2012, 2013]
    id = '5036978'

    for year in years:
        books = stats.bookReadForTheLongestInGivenYear(getbooks.getBooksFromShelfGivenYear(year, id))
        books_list = list(books.values())
        innerlist = list(books_list[0].values())
        longestReadBooks.append([books_list[1], innerlist[0], innerlist[1], innerlist[5], innerlist[6]])
    print(longestReadBooks)





# Draws a graph of the books that took the longest to read
def booksLongestRead():
    daysRead = [28, 189, 306, 136, 1311, 27, 71]
    years = [2011, 2012, 2013, 2014, 2015, 2016, 2017]
    titles = [
                        'Life of Pi',
                        'Venuse delta',
                        'Kadunud vaated',
                        'Holy Sh*t: A Brief History of Swearing',
                        'The Inimitable Jeeves (Jeeves, #2)',
                        'Peopleware: Productive Projects and Teams',
                        'Poésie du gérondif'
                        ]

    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    ax1.set_title("Books that took the longest to read\n")
    ax1.set_ylabel('Days spent reading')
    ax1.set_xlabel('Year finished')

    plt.plot(years, daysRead, 'ro')
    plt.axis([2010, 2018, 0, 1500])

    for x in range(0, len(daysRead)):
        plt.annotate((titles[x] + ' (' + str(daysRead[x]) + ')'),xy=(years[x], daysRead[x]), arrowprops=dict(arrowstyle='->'), xytext=(years[x]-1, daysRead[x]+100))

    plt.show()


count = [3.09, 3.65, 2.79, 3.36, 3.56, 3.41, 3.67]
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017]



# Draws the graph that shows the biggest number of ratings a book read given year has
# Displays years as floats
def mostPopularBooks(count, years):

    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    ax1.set_title("Most popular books\n")
    ax1.set_ylabel('Number of ratings')
    ax1.set_xlabel('Year finished')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])
    plt.grid(True)

    for x in range(0, len(count)):
        plt.annotate((str(count[x])), xy=(years[x], count[x]),xytext=(years[x]-0.5, count[x]-0.5))

    plt.show()


# Draws the graph that shows the smallest number of ratings a book read given year has
# Displays years as floats
def leastPopularBooks(count, years):

    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    ax1.set_title("Least popular books\n")
    ax1.set_ylabel('Number of ratings')
    ax1.set_xlabel('Year finished')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])
    plt.grid(True)

    for x in range(0, len(count)):
        plt.annotate((str(count[x])), xy=(years[x], count[x]),xytext=(years[x]-0.5, count[x]-0.5))

    plt.show()


# Draws the graph that shows the number of ratings a book read in given year has on average
# Displays years as floats
def averageNumberOfRatings(count, years):

    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    ax1.set_title("Average count of ratings\n")
    ax1.set_ylabel('Count')
    ax1.set_xlabel('Year finished')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)+1000])
    plt.grid(True)

    for x in range(0, len(count)):
        plt.annotate((str(count[x])), xy=(years[x], count[x]),xytext=(years[x]-0.5, count[x]-0.5))

    plt.show()


# Draws a graph of worst books read
# Doesn't display titles and displays years as floats
def worstBooks(ratings, years):
    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    ax1.set_title("Worst books read\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    plt.plot(years, ratings, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, 5])
    plt.grid(True)

    for x in range(0, len(ratings)):
        plt.annotate((str(ratings[x])), xy=(years[x], ratings[x]),xytext=(years[x]-0.5, ratings[x]-0.5))

    plt.show()


# Draws a graph of best books read
# Doesn't display titles and displays years as floats
def bestBooks(ratings, years):

    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    ax1.set_title("Best books read\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    plt.plot(years, ratings, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, 5])
    plt.grid(True)

    for x in range(0, len(ratings)):
        plt.annotate((str(ratings[x])), xy=(years[x], ratings[x]),xytext=(years[x]-0.5, ratings[x]-0.5))

    plt.show()


# Draws a graph of average rating of books
# Displays years as floats
def averageRating(ratings, years):

    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    ax1.set_title("Average rating of read books\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    plt.plot(years, ratings, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, 5])
    plt.grid(True)

    for x in range(0, len(ratings)):
        plt.annotate((str(ratings[x])), xy=(years[x], ratings[x]),xytext=(years[x]-0.5, ratings[x]-0.5))

    plt.show()
