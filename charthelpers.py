import matplotlib.pyplot as plt
import matplotlib.ticker
from datetime import datetime
import os


# Helper function for force displaying of integers instead of floats as ticks
def display_integers_as_ticks():
    locator = matplotlib.ticker.MultipleLocator(1)
    plt.gca().xaxis.set_major_locator(locator)
    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
    plt.gca().xaxis.set_major_formatter(formatter)


# Stuff that is common in all line charts
def common_chart_settings(axis_y, axis_x, rating, user_names):
    fig = plt.figure(figsize=(19,10))

    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))
    plt.grid(True)
    plt.style.use('ggplot')

    max_count = 0

    for one_user_data in axis_y:
        print(one_user_data)
        plt.plot(axis_x, one_user_data, linestyle="dashed", marker="o", label=user_names[axis_y.index(one_user_data)][0])
        for x in one_user_data:
            print(x)
            if x > max_count:
                max_count = x

    plt.legend()

    if rating:
        plt.axis([min(axis_x) - 1, max(axis_x) + 1, 0, 5])
    else:
        plt.axis([min(axis_x) - 1, max(axis_x) + 1, 0, max_count * 1.2])

    return ax1


def save_as_image(file_name):
    f = 'images/'+ file_name + '.png'
    os.makedirs(os.path.dirname(f), exist_ok=True)
    plt.savefig('images/' + datetime.now().strftime("%Y%m%d-%H%M%S") + file_name + '.png')