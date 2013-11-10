"""
problem 1.

Plot f(x) = 1 - e ^ (2 * x) over [-1, 1] with intervals .01
"""
from math import exp

from matplotlib import pyplot
from numpy import arange, array


def main():
    x_range = arange(-1, 1.01, .01)
    y_range = array([1 - exp(2 * x) for x in x_range])
    pyplot.plot(x_range, y_range, 'ro')
    pyplot.ylabel("Another label? Goddamnit!")
    pyplot.show()


if __name__ == "__main__":
    main()
