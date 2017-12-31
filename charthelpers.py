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


# Stuff that is common in all charts
def commonChartSettings(y, x, r):
    fig = plt.figure(figsize=(19,10))
    ax1 = fig.add_axes((0.1,0.1,0.8,0.8))
    displayIntegersAsTicks()
    plt.grid(True)
    plt.plot(x, y, linestyle="dashed", marker="o", color="green")
    if r:
        plt.axis([min(x)-1, max(x)+1, 0, 5])
    else:
        plt.axis([min(x)-1, max(x)+1, 0, max(y)*1.2])

    return ax1

def displayIntAndIntAnnotations(y, z):
    for x in range(0, len(y)):
        plt.annotate((str(y[x])), xy=(z[x], y[x]),xytext=(z[x]+0.25, y[x]-0.5))


def displayIntIntStrAnnotations(q, y, z):
    for x in range(0, len(q)):
        plt.annotate((str(q[x]) + '\n ("' + z[x] + '")'), xy=(y[x], q[x]),xytext=(y[x]+0.25, q[x]-0.5))


def displayFloatIntAnnotations(z, y):
    for x in range(0, len(z)):
        plt.annotate(('{0:.2f}'.format(z[x])), xy=(y[x], z[x]),xytext=(y[x]+0.25, z[x]-0.5))


def displayFloatIntStrAnnotations(z, y, q):
    for x in range(0, len(z)):
        plt.annotate((str(z[x]) + '\n ("' + q[x] + '")'), xy=(y[x], z[x]),xytext=(y[x]-0.25, z[x]-0.5))


def saveAsImage(filename):
    f = 'images/'+ filename + '.png'
    os.makedirs(os.path.dirname(f), exist_ok=True)
    plt.savefig('images/' + datetime.now().strftime("%Y%m%d-%H%M%S") + filename + '.png')
