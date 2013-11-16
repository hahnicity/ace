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

from numpy import array, var


def get_yield_and_prob():
    """
    Return the yield and the expectation (probability weight) of each yield
    """
    return array([0.7, 1.3]), array([0.5, 0.5])


def set_gov_support(p, support):
    """
    Given an 1d vector of prices modifies an item if below the price threshold
    """
    for i, x in enumerate(p):
        if x < support:
            p[i] = support


def part_a():
    """
    Compute the variance in price
    """
    a = 1
    y, w = get_yield_and_prob()
    for _ in range(100):
        a_previous = a
        p = 3 - 2 * a * y
        f = w.dot(p)
        a = 0.5 + 0.5 * f
        if fabs(a_previous - a) < exp(-8):
            break
    print "acreage", a, "variance:", var(p), "expectation", p.dot(w)


def part_b():
    """
    Computer part a with gov support factored in
    """
    a = 1
    y, w = get_yield_and_prob()
    for _ in range(100):
        a_previous = a
        p = 3 - 2 * a * y
        set_gov_support(p, 1.0)
        f = w.dot(p)
        a = 0.5 + 0.5 * f
        if fabs(a_previous - a) < exp(-8):
            break
    print "acreage", a, "variance:", var(p), "expectation", p.dot(w)


def main():
    part_a()
    part_b()


if __name__ == "__main__":
    main()
