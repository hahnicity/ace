"""
Consider the original example with the farmer where acreage planted will be

a = 0.5 + 0.5 * Ep (Ep is expected price)

Quantity q is equivalent to

q = a * y (y is yield)

Clearing price p is

p = 3 - 2 * q

Assume in our case that yield will be a random two point distribution s.t.

y = array([0.7, 1.3])

Our goal is to compute the variance of this price distribution, otherwise known
as sigma^2 for part a.
"""
from math import exp, fabs

from numpy import array, transpose


def part_a():
    """
    Compute the variance in price
    """
    y = array([0.7, 1.3])
    w = array([0.5, 0.5])  # The expectation (probability weight) of each yield
    a = 1
    for _ in range(100):
        a_previous = a
        p = 3 - 2 * a * y
        f = w.dot(p)
        a = 0.5 + 0.5 * f
        print a, f
        if fabs(a_previous - a) < exp(-8):
            break
    print a, f, w * p, p


def main():
    part_a()


if __name__ == "__main__":
    main()
