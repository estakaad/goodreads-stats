import matplotlib.pyplot as plt
import matplotlib.ticker
import charts
from datetime import datetime
import os


# Helper function for force displaying of integers instead of floats as ticks
def displayIntegersAsTicks():
    locator = matplotlib.ticker.MultipleLocator(1)
    plt.gca().xaxis.set_major_locator(locator)
    formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
    plt.gca().xaxis.set_major_formatter(formatter)


# Stuff that is common in all line charts
def commonChartSettings(axisy, axisx, rating, usernames):
    fig = plt.figure(figsize=(19,10))

    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))
    plt.grid(True)
    plt.style.use('ggplot')

    maxCount = 0

    for oneUserData in axisy:
        print(oneUserData)
        plt.plot(axisx, oneUserData, linestyle="dashed", marker="o", label=usernames[axisy.index(oneUserData)][0])
        for x in oneUserData:
            print(x)
            if x > maxCount:
                maxCount = x

    plt.legend()

    if rating:
        plt.axis([min(axisx)-1, max(axisx)+1, 0, 5])
    else:
        plt.axis([min(axisx)-1, max(axisx)+1, 0, maxCount*1.2])

    return ax1

def displayIntAndIntAnnotations(y, z):
    for x in range(0, len(y)):
        plt.annotate((str(y[x])), xy=(z[x], y[x]),xytext=(z[x]+0.25, y[x]-0.5))


def displayIntIntStrAnnotations(axisXInt, axisYInt, string):
    for x in range(0, len(axisXInt)):
        if string[x] != '-':
            plt.annotate((str(axisXInt[x]) + '\n ("' + string[x] + '")'), xy=(axisYInt[x], axisXInt[x]),xytext=(axisYInt[x]-0.25, axisXInt[x]+0.7))
        else:
            plt.annotate((str(axisXInt[x])), xy=(axisYInt[x], axisXInt[x]),xytext=(axisYInt[x]-0.25, axisXInt[x]+0.7))


def displayFloatIntAnnotations(z, y):
    for x in range(0, len(z)):
        plt.annotate(('{0:.2f}'.format(z[x])), xy=(y[x], z[x]),xytext=(y[x]+0.25, z[x]-0.5))


def displayFloatIntStrAnnotations(z, y, q):
    for x in range(0, len(z)):
        if q[x] != '-':
            plt.annotate((str(z[x]) + '\n ("' + q[x] + '")'), xy=(y[x], z[x]),xytext=(y[x]-0.25, z[x]-0.5))
        else:
            plt.annotate((str(z[x])), xy=(y[x], z[x]),xytext=(y[x]-0.25, z[x]-0.5))


def saveAsImage(filename):
    f = 'images/'+ filename + '.png'
    os.makedirs(os.path.dirname(f), exist_ok=True)
    plt.savefig('images/' + datetime.now().strftime("%Y%m%d-%H%M%S") + filename + '.png')
