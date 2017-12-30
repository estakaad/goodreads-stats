import matplotlib.pyplot as plt
import stats
import getbooks
import view
import matplotlib.ticker

# Helper function for force displaying of integers instead of floats as ticks
def displayIntegersAsTicks():
    locator = matplotlib.ticker.MultipleLocator(1)
    plt.gca().xaxis.set_major_locator(locator)
    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
    plt.gca().xaxis.set_major_formatter(formatter)


# Stuff that is common in all charts
def commonChartSettings():
    fig = plt.figure()
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))
    displayIntegersAsTicks()
    plt.grid(True)

    return ax1

def displayIntAndIntAnnotations(y, z):
    for x in range(0, len(y)):
        plt.annotate((str(y[x])), xy=(z[x], y[x]),xytext=(z[x]+0.25, y[x]-0.5))


def displayIntIntStrAnnotations(q, y, z):
    for x in range(0, len(q)):
        plt.annotate((str(q[x]) + '\n ("' + z[x] + '"")'), xy=(y[x], q[x]),xytext=(y[x]+0.25, q[x]-0.5))


def displayFloatIntAnnotations(z, y):
    for x in range(0, len(z)):
        plt.annotate(('{0:.2f}'.format(z[x])), xy=(y[x], z[x]),xytext=(y[x]+0.25, z[x]-0.5))


def displayFloatIntStrAnnotations(z, y, q):
    for x in range(0, len(z)):
        plt.annotate((str(z[x]) + '\n ("' + q[x] + '"")'), xy=(y[x], z[x]),xytext=(y[x]-0.25, z[x]-0.5))


# Draws a graph of the books that took the longest to finish
def longestReadBooks(days, years, titles):

    ax1 = commonChartSettings()
    ax1.set_title("Books that took the longest to read\n")
    ax1.set_ylabel('Days')
    ax1.set_xlabel('Year finished')

    plt.plot(years, days, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(days)*1.2])

    displayIntIntStrAnnotations(days, years, titles)

    plt.show()


# Draws the graph that shows how many pages were read in a given year
def totalPagesRead(count, years):
    ax1 = commonChartSettings()

    ax1.set_title("Pages read\n")
    ax1.set_ylabel('Number of pages')
    ax1.set_xlabel('Year')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])

    displayIntAndIntAnnotations(count, years)

    plt.show()


# Draws the graph that shows how many pages were read on an average day
def averageNumberOfPages(count, years):

    ax1 = commonChartSettings()

    ax1.set_title("Pages read per day\n")
    ax1.set_ylabel('Number of pages')
    ax1.set_xlabel('Year')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])

    displayFloatIntAnnotations(count, years)

    plt.show()


# Draws the graph that shows the biggest number of ratings a book read given year has
def mostPopularBooks(count, years, titles):

    ax1 = commonChartSettings()

    ax1.set_title("Most popular books read\n")
    ax1.set_ylabel('Number of ratings')
    ax1.set_xlabel('Year finished')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])

    displayIntIntStrAnnotations(count, years, titles)

    plt.show()


# Draws the graph that shows the smallest number of ratings a book read given year has
def leastPopularBooks(count, years, titles):

    ax1 = commonChartSettings()

    ax1.set_title("Least popular books read\n")
    ax1.set_ylabel('Number of ratings')
    ax1.set_xlabel('Year finished')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])

    displayIntIntStrAnnotations(count, years, titles)

    plt.show()


# Draws the graph that shows the number of ratings a book read in given year has on average
def averageNumberOfRatings(count, years):

    ax1 = commonChartSettings()

    ax1.set_title("Average count of ratings\n")
    ax1.set_ylabel('Count')
    ax1.set_xlabel('Year finished')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])

    displayFloatIntAnnotations(count, years)

    plt.show()


# Draws a graph of worst books read
def worstBooks(ratings, years, titles):

    ax1 = commonChartSettings()

    ax1.set_title("Worst books read\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    plt.plot(years, ratings, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, 5])

    displayFloatIntStrAnnotations(ratings, years, titles)

    plt.show()


# Draws a graph of best books read
def bestBooks(ratings, years, titles):

    ax1 = commonChartSettings()

    ax1.set_title("Best books read\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    plt.plot(years, ratings, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, 5])

    displayFloatIntStrAnnotations(ratings, years, titles)

    plt.show()


# Draws a graph of average rating of books
def averageRating(ratings, years):

    ax1 = commonChartSettings()

    ax1.set_title("Average rating of read books\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    plt.plot(years, ratings, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, 5])

    displayFloatIntAnnotations(ratings, years)

    plt.show()
