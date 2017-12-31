import matplotlib.pyplot as plt
import stats
import getbooks
import view
import charthelpers as ch
import numpy as np

# Draws a line chart of the books that took the longest to finish.
def longestReadBooks(days, years, titles):
    r = False
    ax1 = ch.commonLineChartSettings(days, years, r)
    ax1.set_title("Books that took the longest to read\n")
    ax1.set_ylabel('Days')
    ax1.set_xlabel('Year finished')

    ch.displayIntIntStrAnnotations(days, years, titles)
    ch.saveAsImage('_longest_read_books')


# Draws a line chart showing how many pages were read in a given year.
def totalPagesRead(count, years):
    r = False
    ax1 = ch.commonLineChartSettings(count, years, r)
    ax1.set_title("Pages read\n")
    ax1.set_ylabel('Number of pages')
    ax1.set_xlabel('Year')

    ch.displayIntAndIntAnnotations(count, years)
    ch.saveAsImage('_total_pages_read')


# Draws a line chart showing how many pages were read on an average day.
def averageNumberOfPages(count, years):
    r = False
    ax1 = ch.commonLineChartSettings(count, years, r)
    ax1.set_title("Pages read per day\n")
    ax1.set_ylabel('Number of pages')
    ax1.set_xlabel('Year')

    ch.displayFloatIntAnnotations(count, years)
    ch.saveAsImage('_average_num_pages_per_day')


# Draws a line chart showing the most popular books read.
# Most popular here means having the highest number of ratings on Goodreads.
def mostPopularBooks(count, years, titles):
    r = False
    ax1 = ch.commonLineChartSettings(count, years, r)
    ax1.set_title("Most popular books read\n")
    ax1.set_ylabel('Number of ratings')
    ax1.set_xlabel('Year finished')

    ch.displayIntIntStrAnnotations(count, years, titles)
    ch.saveAsImage('_most_popular_books')


# Draws a line chart showing the least popular books read.
# Least popular here means having the lowest number of ratings on Goodreads.
def leastPopularBooks(count, years, titles):
    r = False
    ax1 = ch.commonLineChartSettings(count, years, r)
    ax1.set_title("Least popular books read\n")
    ax1.set_ylabel('Number of ratings')
    ax1.set_xlabel('Year finished')

    ch.displayIntIntStrAnnotations(count, years, titles)
    ch.saveAsImage('_least_popular_books')


# Draws a line chart showing the number of ratings a book read in given year had on average.
def averageNumberOfRatings(count, years):
    r = False
    ax1 = ch.commonLineChartSettings(count, years, r)
    ax1.set_title("Average count of ratings\n")
    ax1.set_ylabel('Count')
    ax1.set_xlabel('Year finished')

    ch.displayFloatIntAnnotations(count, years)
    ch.saveAsImage('_average_number_of_ratings')


# Draws a line chart of worst books read.
# Worst here means having the lowest rating on Goodreads.
def worstBooks(ratings, years, titles):
    r = True
    ax1 = ch.commonLineChartSettings(ratings, years, r)
    ax1.set_title("Worst books read\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    ch.displayFloatIntStrAnnotations(ratings, years, titles)
    ch.saveAsImage('_worst_books')


# Draws a line chart of best books read.
# Best here means having the highest rating on Goodreads.
def bestBooks(ratings, years, titles):
    r = True
    ax1 = ch.commonLineChartSettings(ratings, years, r)
    ax1.set_title("Best books read\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    ch.displayFloatIntStrAnnotations(ratings, years, titles)
    ch.saveAsImage('_best_books')


# Draws a line graph of average rating of read books.
def averageRating(ratings, years):
    r = True
    ax1 = ch.commonLineChartSettings(ratings, years, r)
    ax1.set_title("Average rating of read books\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    ch.displayFloatIntAnnotations(ratings, years)
    ch.saveAsImage('_average_rating')


def daysReadAndPages(days, pages):
    fig = plt.figure(figsize=(19,10))
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    plt.style.use('ggplot')

    N = len(pages)
    x = pages
    y = days
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    ch.saveAsImage('_days_read_and_pages')


def daysReadAndRatings(days, ratings):
    fig = plt.figure(figsize=(19,10))
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))

    plt.style.use('ggplot')

    N = len(ratings)
    x = ratings
    y = days
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    ch.saveAsImage('_days_read_and_ratings')
