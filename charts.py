import matplotlib.pyplot as plt
import stats
import getbooks
import view
import charthelpers as ch


# Draws a line chart of the books that took the longest to finish.
def longestReadBooks(days, years, titles):

    ax1 = ch.commonChartSettings()
    ax1.set_title("Books that took the longest to read\n")
    ax1.set_ylabel('Days')
    ax1.set_xlabel('Year finished')

    plt.plot(years, days, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(days)*1.2])

    ch.displayIntIntStrAnnotations(days, years, titles)

    plt.show()


# Draws a line chart showing how many pages were read in a given year.
def totalPagesRead(count, years):
    ax1 = ch.commonChartSettings()

    ax1.set_title("Pages read\n")
    ax1.set_ylabel('Number of pages')
    ax1.set_xlabel('Year')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])

    ch.displayIntAndIntAnnotations(count, years)

    plt.show()


# Draws a line chart showing how many pages were read on an average day.
def averageNumberOfPages(count, years):

    ax1 = ch.commonChartSettings()

    ax1.set_title("Pages read per day\n")
    ax1.set_ylabel('Number of pages')
    ax1.set_xlabel('Year')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])

    ch.displayFloatIntAnnotations(count, years)

    plt.show()


# Draws a line chart showing the most popular books read.
# Most popular here means having the highest number of ratings on Goodreads.
def mostPopularBooks(count, years, titles):

    ax1 = ch.commonChartSettings()

    ax1.set_title("Most popular books read\n")
    ax1.set_ylabel('Number of ratings')
    ax1.set_xlabel('Year finished')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])

    ch.displayIntIntStrAnnotations(count, years, titles)

    plt.show()


# Draws a line chart showing the least popular books read.
# Least popular here means having the lowest number of ratings on Goodreads.
def leastPopularBooks(count, years, titles):

    ax1 = ch.commonChartSettings()

    ax1.set_title("Least popular books read\n")
    ax1.set_ylabel('Number of ratings')
    ax1.set_xlabel('Year finished')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])

    ch.displayIntIntStrAnnotations(count, years, titles)

    plt.show()


# Draws a line chart showing the number of ratings a book read in given year had on average.
def averageNumberOfRatings(count, years):

    ax1 = ch.commonChartSettings()

    ax1.set_title("Average count of ratings\n")
    ax1.set_ylabel('Count')
    ax1.set_xlabel('Year finished')

    plt.plot(years, count, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, max(count)*1.2])

    ch.displayFloatIntAnnotations(count, years)

    plt.show()


# Draws a line chart of worst books read.
# Worst here means having the lowest rating on Goodreads.
def worstBooks(ratings, years, titles):

    ax1 = ch.commonChartSettings()

    ax1.set_title("Worst books read\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    plt.plot(years, ratings, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, 5])

    ch.displayFloatIntStrAnnotations(ratings, years, titles)

    plt.show()


# Draws a line chart of best books read.
# Best here means having the highest rating on Goodreads.
def bestBooks(ratings, years, titles):

    ax1 = ch.commonChartSettings()

    ax1.set_title("Best books read\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    plt.plot(years, ratings, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, 5])

    ch.displayFloatIntStrAnnotations(ratings, years, titles)

    plt.show()


# Draws a line graph of average rating of read books.
def averageRating(ratings, years):

    ax1 = ch.commonChartSettings()

    ax1.set_title("Average rating of read books\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    plt.plot(years, ratings, linestyle="dashed", marker="o", color="green")
    plt.axis([min(years)-1, max(years)+1, 0, 5])

    ch.displayFloatIntAnnotations(ratings, years)

    plt.show()
