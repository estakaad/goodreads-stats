import stats
import getbooks
import prettytable
import charts

all_users_values = []
all_user_names = []


def ask_for_id():

    while True:
        try:
            ids = [int(x) for x in input('\nEnter Goodreads\' users\' ID\'s separated by spaces.\n').split()]
            break
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
    return ids


def ask_for_years():

    while True:
        try:
            years = [int(x) for x in input('\nEnter the years you want to analyze separated by spaces.\n').split()]
            break
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
    return years


def display_questions():

    print('Choose a question and enter the letter in front of it or enter q to quit.\n')

    table = prettytable.PrettyTable(['Option', 'Question'])

    questions = [
                 ['a', 'Which book took the longest to read?'],
                 ['b', 'How many pages did I read in year x?'],
                 ['c', 'How many pages did I read on an average day in year x?'],
                 ['d', 'Which was the most popular book I read in year x?'],
                 ['e', 'Which was the least popular book I read in year x?'],
                 ['f', 'How popular was an average book I read in year x?'],
                 ['g', 'What was the worst book I read in year x?'],
                 ['h', 'What was the best book I read in year x?'],
                 ['i', 'How good was the average book I read in year x?'],
                 ['j', 'Show me all the answers!']
                ]

    for question in questions:
        table.add_row(question)

    table.align = 'l'
    print(table)


def ask_loading_from_file():

    option = input('Do you want to load the books from a file? y/n \n')

    if option == 'y':
        return True

    return False


def add_user_name_and_other_values_to_list(user_names, count, user_count, years, create_chart):

    for user_name in user_names:
        if user_name == '':
            user_names.remove(user_name)
    user_names = list(set(user_names))

    all_users_values.append(count)
    all_user_names.append(user_names)

    if len(all_users_values) == user_count:
        create_chart(all_users_values, years, all_user_names)
        all_users_values.clear()
        all_user_names.clear()


def display_longest_read_books(years, id, from_file, user_count):

    x = prettytable.PrettyTable(['Days read', 'Title', 'Author', 'Started', 'Finished'])
    days = []
    titles = []
    user_names = []
    x.align = 'l'

    for year in years:
        books = stats.book_read_for_the_longest_in_given_year(getbooks.get_books_from_shelf_given_year(year, id, from_file))
        if len(books) != 0:
            books_list = list(books.values())
            inner_list = list(books_list[0].values())
            x.add_row([books_list[1], inner_list[0], inner_list[1], inner_list[5], inner_list[6]])
            days.append(books_list[1])
            titles.append(inner_list[0])
        else:
            x.add_row(['-', '-', '-', '-', '-'])
            days.append(0)
            titles.append('-')
        user_names.append(inner_list[7])

    print('BOOKS THAT TOOK THE LONGEST TO FINISH')
    print(x)

    add_user_name_and_other_values_to_list(user_names, days, user_count, years, charts.longest_read_books)


def display_total_pages(years, id, from_file, user_count):

    x = prettytable.PrettyTable(['Pages', 'Year'])
    x.align = 'l'
    count = []
    user_names = []
    for year in years:
        users_pages = stats.total_pages_read_given_year(getbooks.get_books_from_shelf_given_year(year, id, from_file))
        x.add_row([users_pages[0], year])
        count.append(int(users_pages[0]))
        user_names.append(users_pages[1])

    print('TOTAL NUMBER OF PAGES READ')
    print(x)

    add_user_name_and_other_values_to_list(user_names, count, user_count, years, charts.total_pages_read)


def display_average_pages_per_day(years, id, from_file, user_count):

    x = prettytable.PrettyTable(['Pages per day', 'Year'])
    count = []
    user_names = []
    x.align = 'l'
    for year in years:
        pages = stats.average_number_of_pages_read_in_day(getbooks.get_books_from_shelf_given_year(year, id, from_file), year)
        x.add_row(['{0:.2f}'.format(float(pages[0])), year])
        count.append(pages[0])
        user_names.append(pages[1])

    print('AVERAGE NUMBER OF PAGES READ PER DAY')
    print(x)

    add_user_name_and_other_values_to_list(user_names, count, user_count, years, charts.average_number_of_pages)


def display_most_popular_books(years, id, from_file, user_count):

    x = prettytable.PrettyTable(['Number of ratings', 'Title', 'Author', 'Started', 'Finished'])
    count = []
    titles = []
    user_names = []
    x.align = 'l'
    for year in years:
        books = stats.book_with_most_ratings_in_given_year(getbooks.get_books_from_shelf_given_year(year, id, from_file))
        if len(books) != 0:
            books_list = list(books.values())
            inner_list = list(books_list[0].values())
            x.add_row([inner_list[4], inner_list[0], inner_list[1], inner_list[5], inner_list[6]])
            count.append(int(inner_list[4]))
            titles.append(inner_list[0])
        else:
            x.add_row(['-', '-', '-', '-', '-'])
            count.append(0)
            titles.append('-')
        user_names.append(inner_list[7])

    print('MOST POPULAR BOOKS READ (POPULAR = BOOKS WITH THE HIGHEST NUMBER OF RATINGS)')
    print(x)

    add_user_name_and_other_values_to_list(user_names, count, user_count, years, charts.most_popular_books)


def display_least_popular_books(years, id, from_file, user_count):

    x = prettytable.PrettyTable(['Number of ratings', 'Title', 'Author', 'Started', 'Finished'])
    count = []
    titles = []
    user_names = []
    x.align = 'l'
    for year in years:
        books = stats.book_with_least_ratings_in_given_year(getbooks.get_books_from_shelf_given_year(year, id, from_file))
        if len(books) != 0:
            books_list = list(books.values())
            inner_list = list(books_list[0].values())
            x.add_row([inner_list[4], inner_list[0], inner_list[1], inner_list[5], inner_list[6]])
            count.append(int(inner_list[4]))
            titles.append(inner_list[0])
        else:
            x.add_row(['-', '-', '-', '-', '-'])
            count.append(0)
            titles.append('-')
        user_names.append(inner_list[7])

    print('LEAST POPULAR BOOKS READ (LEAST POPULAR = BOOKS WITH THE LOWEST NUMBER OF RATINGS)')
    print(x)

    add_user_name_and_other_values_to_list(user_names, count, user_count, years, charts.least_popular_books)


def display_average_number_of_ratings(years, id, from_file, user_count):

    x = prettytable.PrettyTable(['Average ratings count', 'Year'])
    count = []
    user_names = []
    x.align = 'l'
    for year in years:
        ratings = stats.average_number_of_ratings(getbooks.get_books_from_shelf_given_year(year, id, from_file))
        x.add_row(['{0:.2f}'.format(float(ratings[0])), year])
        count.append(ratings[0])
        user_names.append(ratings[1])

    print('AVERAGE NUMBER OF RATINGS OF BOOKS READ')
    print(x)

    add_user_name_and_other_values_to_list(user_names, count, user_count, years, charts.average_number_of_ratings)


def display_worst_books(years, id, from_file, user_count):

    x = prettytable.PrettyTable(['Rating', 'Title', 'Author', 'Started', 'Finished'])
    ratings = []
    titles = []
    user_names = []
    x.align = 'l'
    for year in years:
        books = stats.worst_book_read(getbooks.get_books_from_shelf_given_year(year, id, from_file))
        if len(books) != 0:
            books_list = list(books.values())
            inner_list = list(books_list[0].values())
            x.add_row([inner_list[3], inner_list[0], inner_list[1], inner_list[5], inner_list[6]])
            ratings.append(float(inner_list[3]))
            titles.append(inner_list[0])
        else:
            x.add_row(['-', '-', '-', '-', '-'])
            ratings.append(0)
            titles.append('-')
        user_names.append(inner_list[7])

    print('WORST BOOKS READ')
    print(x)

    add_user_name_and_other_values_to_list(user_names, ratings, user_count, years, charts.worst_books)


def display_best_books(years, id, from_file, user_count):

    x = prettytable.PrettyTable(['Rating', 'Title', 'Author', 'Started', 'Finished'])
    ratings = []
    titles = []
    user_names = []
    x.align = 'l'
    for year in years:
        books = stats.best_book_read(getbooks.get_books_from_shelf_given_year(year, id, from_file))
        if len(books) != 0:
            books_list = list(books.values())
            inner_list = list(books_list[0].values())
            x.add_row([inner_list[3], inner_list[0], inner_list[1], inner_list[5], inner_list[6]])
            ratings.append(float(inner_list[3]))
            titles.append(inner_list[0])
        else:
            x.add_row(['-', '-', '-', '-', '-'])
            ratings.append(0)
            titles.append('-')
        user_names.append(inner_list[7])

    print('BEST BOOKS READ')
    print(x)

    add_user_name_and_other_values_to_list(user_names, ratings, user_count, years, charts.best_books)


def display_average_rating(years, id, from_file, user_count):

    x = prettytable.PrettyTable(['Average rating', 'Year'])
    ratings = []
    x.align = 'l'
    user_names = []
    for year in years:
        average_rating = stats.average_rating_of_book(getbooks.get_books_from_shelf_given_year(year, id, from_file))
        x.add_row(['{0:.2f}'.format(float(average_rating[0])), year])
        ratings.append(float(average_rating[0]))
        user_names.append(average_rating[1])

    print('AVERAGE RATING OF BOOKS READ')
    print(x)

    add_user_name_and_other_values_to_list(user_names, ratings, user_count, years, charts.average_rating)
