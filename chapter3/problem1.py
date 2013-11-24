"""
Do Newton's method for

x = x^2 - c
"""


def newtons_for_func(c, x, iterations=100):
    """
    Given some value c > 0 solve the root for the newton's method
    equation x = x^2 - c
    """
    for _ in xrange(iterations):
        x = x - (1.0 / (2.0 * x)) * (x ** 2.0 - c)
    return x


def part_a():
    """
    I'm going to start writing down results that normally would be
    done on paper in the computer
    """
    x = x - (1.0 / (2.0 * x)) * (x ** 2 - c)


def part_b():
    """
    So we are asked how would we go about finding a starting point for
    newton's method.

    In the most basic sense we can provide a guess of where the function
    f(x) = 0. We can also use the bisection method and iterate > 10 times
    to provide a more accurate guess.
    """
    pass


def part_c():
    for c in xrange(1, 100):
        print newtons_for_func(c, 1, iterations=10)


def main():
    part_c()


if __name__ == "__main__":
    main()
