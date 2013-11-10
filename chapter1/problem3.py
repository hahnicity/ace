"""
Problem 3.

calculate the time series

yt = 5 + .05 * t + Et (Where E is epsilon)

for years 1960, 1961, ..., 2001 assuming Et independently and
identically distributed with mean 0 and sigma 0.2.
"""
from random import uniform

from matplotlib.pyplot import plot, show
from numpy import array, polyfit, poly1d


def create_distribution(size):
    """
    Create a distribution, identically distributed, with mean 0 and
    sigma 0.2
    """
    # Shit it's way easier to just do some uniform distribution
    # This is a bit over my head, and not possible for me without
    # pen and paper
    return array([uniform(-0.2, .2) for _ in xrange(size)])


def create_time_series(start_year, end_year):
    """
    Create the time series, yt, then perform a regress on yt, plot yt and the
    its trendline
    """
    t_array = array(range(start_year, end_year + 1))
    epsilon_t = create_distribution(len(t_array))
    yt = array([5 + .05 * t_i + epsilon_t[i] for i, t_i in enumerate(t_array)])
    fit = polyfit(t_array, yt, 1)
    fit_func = poly1d(fit)
    plot(t_array, yt, "yo", t_array, fit_func(t_array), "--k")
    show()


def main():
    create_time_series(1960, 2001)


if __name__ == "__main__":
    main()
