"""
Compare Newton's method against Broydens method in R2
"""
from numpy import array
from numpy.linalg import inv


def part_a(x, iterations=1000):
    """
    Calculate the two functions using newtons method
    """
    f = lambda x1, x2: array(
        [200 * x1 * (x2 - x1 ** 2) - x1 + 1, 100 * (x1 ** 2 - x2)]
    )
    J = lambda x1, x2: array([
        [200 * x2 - 600 * x1 ** 2 - 1, 200 * x2],
        [200 * x1, -100],
    ])
    for _ in xrange(iterations):
        x = x - inv(J(x[0], x[1])).dot(f(x[0], x[1]))
    return x


def main():
    print part_a(array([2.0, 1.5]))


if __name__ == "__main__":
    main()
