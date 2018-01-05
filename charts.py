import charthelpers as ch


# Draws a line chart of the books that took the longest to finish.
def longest_read_books(days, years, user_names):
    r = False

    ax1 = ch.common_chart_settings(days, years, r, user_names)
    ax1.set_title("Books that took the longest to read\n")
    ax1.set_ylabel('Days')
    ax1.set_xlabel('Year finished')
    # ch.displayIntIntStrAnnotations(days, years)
    ch.display_integers_as_ticks()
    ch.save_as_image('_longest_read_books')


# Draws a line chart showing how many pages were read in a given year.
def total_pages_read(count, years, user_names):
    r = False

    ax1 = ch.common_chart_settings(count, years, r, user_names)
    ax1.set_title("Pages read\n")
    ax1.set_ylabel('Number of pages')
    ax1.set_xlabel('Year')
    ch.display_integers_as_ticks()
    ch.save_as_image('_total_pages_read')


# Draws a line chart showing how many pages were read on an average day.
def average_number_of_pages(count, years, user_names):
    r = False

    ax1 = ch.common_chart_settings(count, years, r, user_names)
    ax1.set_title("Pages read per day\n")
    ax1.set_ylabel('Number of pages')
    ax1.set_xlabel('Year')

    # ch.displayFloatIntAnnotations(count, years)
    ch.display_integers_as_ticks()
    ch.save_as_image('_average_num_pages_per_day')


# Draws a line chart showing the most popular books read.
# Most popular here means having the highest number of ratings on Goodreads.
def most_popular_books(count, years, user_names):
    r = False

    ax1 = ch.common_chart_settings(count, years, r, user_names)
    ax1.set_title("Most popular books read\n")
    ax1.set_ylabel('Number of ratings')
    ax1.set_xlabel('Year finished')

    # ch.displayIntIntStrAnnotations(count, years)
    ch.display_integers_as_ticks()
    ch.save_as_image('_most_popular_books')


# Draws a line chart showing the least popular books read.
# Least popular here means having the lowest number of ratings on Goodreads.
def least_popular_books(count, years, user_names):
    r = False

    ax1 = ch.common_chart_settings(count, years, r, user_names)
    ax1.set_title("Least popular books read\n")
    ax1.set_ylabel('Number of ratings')
    ax1.set_xlabel('Year finished')

    ch.display_integers_as_ticks()
    ch.save_as_image('_least_popular_books')


# Draws a line chart showing the number of ratings a book read in given year had on average.
def average_number_of_ratings(count, years, user_names):
    print(count)
    print(user_names)
    r = False

    ax1 = ch.common_chart_settings(count, years, r, user_names)
    ax1.set_title("Average count of ratings\n")
    ax1.set_ylabel('Count')
    ax1.set_xlabel('Year finished')

    # ch.displayFloatIntAnnotations(count, years)
    ch.display_integers_as_ticks()
    ch.save_as_image('_average_number_of_ratings')


# Draws a line chart of worst books read.
# Worst here means having the lowest rating on Goodreads.
def worst_books(ratings, years, user_names):
    r = True

    ax1 = ch.common_chart_settings(ratings, years, r, user_names)
    ax1.set_title("Worst books read\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    # ch.displayFloatIntStrAnnotations(ratings, years, titles)
    ch.display_integers_as_ticks()
    ch.save_as_image('_worst_books')


# Draws a line chart of best books read.
# Best here means having the highest rating on Goodreads.
def best_books(ratings, years, user_names):
    r = True

    ax1 = ch.common_chart_settings(ratings, years, r, user_names)
    ax1.set_title("Best books read\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    # ch.displayFloatIntStrAnnotations(ratings, years, titles)
    ch.display_integers_as_ticks()
    ch.save_as_image('_best_books')


# Draws a line graph of average rating of read books.
def average_rating(ratings, years, user_names):
    r = True

    ax1 = ch.common_chart_settings(ratings, years, r, user_names)
    ax1.set_title("Average rating of read books\n")
    ax1.set_ylabel('Rating')
    ax1.set_xlabel('Year finished')

    # ch.displayFloatIntStrAnnotations(ratings, years, titles)
    ch.display_integers_as_ticks()
    ch.save_as_image('_average_rating')
