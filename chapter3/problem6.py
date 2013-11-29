"""
Calculate quantile func using the bisection method
"""
from math import fabs
from warnings import warn

from scipy.stats import norm


def icdf(p, func, a, b, tol=1 * 10 ** -6, iterations=100):
    x = (a + b) / 2.0
    d = (b - a) / 2.0
    for _ in xrange(iterations):
        result = func(x) - p
        d = d / 2
        if fabs(result) < tol:
            return x
        elif result > 0:
            x = x - d
        else:
            x = x + d
    else:
        warn("We were unable to find a value suitably close to {} after {} iterations"
             "".format(p, iterations))
        return x


def main():
    print icdf(.6, norm.cdf, -10, 10)


if __name__ == "__main__":
    main()
