import view

ids = view.ask_for_id()
years = view.ask_for_years()
from_file = view.ask_loading_from_file()
view.display_questions()
q = ''

while q != 'q':

    q = input().lower()

    if q == 'a':
        for id in ids:
            view.display_longest_read_books(years, id, from_file, len(ids))
    elif q == 'b':
        for id in ids:
            view.display_total_pages(years, id, from_file, len(ids))
    elif q == 'c':
        for id in ids:
            view.display_average_pages_per_day(years, id, from_file, len(ids))
    elif q == 'd':
        for id in ids:
            view.display_most_popular_books(years, id, from_file, len(ids))
    elif q == 'e':
        for id in ids:
            view.display_least_popular_books(years, id, from_file, len(ids))
    elif q == 'f':
        for id in ids:
            view.display_average_number_of_ratings(years, id, from_file, len(ids))
    elif q == 'g':
        for id in ids:
            view.display_worst_books(years, id, from_file, len(ids))
    elif q == 'h':
        for id in ids:
            view.display_best_books(years, id, from_file, len(ids))
    elif q == 'i':
        for id in ids:
            view.display_average_rating(years, id, from_file, len(ids))
    elif q == 'j':
        for id in ids:
            view.display_longest_read_books(years, id, from_file, len(ids))
        for id in ids:
            view.display_total_pages(years, id, from_file, len(ids))
        for id in ids:
            view.display_average_pages_per_day(years, id, from_file, len(ids))
        for id in ids:
            view.display_most_popular_books(years, id, from_file, len(ids))
        for id in ids:
            view.display_least_popular_books(years, id, from_file, len(ids))
        for id in ids:
            view.display_average_number_of_ratings(years, id, from_file, len(ids))
        for id in ids:
            view.display_worst_books(years, id, from_file, len(ids))
        for id in ids:
            view.display_best_books(years, id, from_file, len(ids))
        for id in ids:
            view.display_average_rating(years, id, from_file, len(ids))
    elif q == 'q':
        break
    else:
        print('You should\'ve followed the instructions.')