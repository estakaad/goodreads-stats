import matplotlib.pyplot as plt
import stats
import getbooks
import view

# Draws a graph of the books that took the longest to finish
# Doesn't display titles and displays years as floats
def longestReadBooks(days, years):
    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    ax1.set_title("Longest read books\n")
    ax1.set_ylabel('Days')
    ax1.set_xlabel('Year finished')

    plt.plot(years, days, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(days)*1.2])
    plt.grid(True)

    for x in range(0, len(days)):
        plt.annotate((str(days[x])), xy=(years[x], days[x]),xytext=(years[x]-0.5, days[x]-0.5))

    plt.show()


# Draws the graph that shows how many pages were read in a given year
# Displays years as floats
def totalPagesRead(count, years):

    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    ax1.set_title("Pages read\n")
    ax1.set_ylabel('Pages')
    ax1.set_xlabel('Year')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])
    plt.grid(True)

    for x in range(0, len(count)):
        plt.annotate((str(count[x])), xy=(years[x], count[x]),xytext=(years[x]-0.5, count[x]-0.5))

    plt.show()


# Draws the graph that shows how many pages were read on an average day
# Displays years as floats
def averageNumberOfPages(count, years):
    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    ax1.set_title("Pages read per day\n")
    ax1.set_ylabel('Count')
    ax1.set_xlabel('Year')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])
    plt.grid(True)

    for x in range(0, len(count)):
        plt.annotate(('{0:.2f}'.format(count[x])), xy=(years[x], count[x]),xytext=(years[x]-0.5, count[x]-0.5))

    plt.show()


# Draws the graph that shows the biggest number of ratings a book read given year has
# Doesn't display titles and displays years as floats
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
# Doesn't display titles and displays years as floats
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
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])
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
