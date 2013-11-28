"""
Compare Newton's method against Broydens method in R2
"""
from numpy import array, transpose
from numpy.linalg import inv


def get_f(x):
    """
    Get f(x)
    """
    f = lambda x1, x2: array(
        [200 * x1 * (x2 - x1 ** 2) - x1 + 1, 100 * (x1 ** 2 - x2)]
    )
    return f(x[0], x[1])


def get_j(x):
    """
    Get the jacobian for newtons method
    """
    J = lambda x1, x2: array([
        [200 * x2 - 600 * x1 ** 2 - 1, 200 * x2],
        [200 * x1, -100],
    ])
    return J(x[0], x[1])


def part_a(x, iterations=100):
    """
    Calculate the two functions using newtons method
    """
    for _ in xrange(iterations):
        f, J = get_f(x), get_j(x)
        x = x - inv(J).dot(f)
    return x


def part_b(x_prev, x_new, J, iterations=100):
    """
    Find a root using Broydens method
    """
    for _ in xrange(iterations):
        d = x_new - x_prev
        g = get_f(x_new) - get_f(x_prev)
        # Calculate Broyden's Jacobian
        J = J + (g - J.dot(d)).dot(transpose(d) / (transpose(d).dot(d)))
        x_new_plus = x_new - inv(J).dot(get_f(x_new))
        x_prev = x_new
        x_new = x_new_plus
    return x_new


def main():
    # For some reason this isn't converging for x1 > 1 x2 > 1.
    print part_a(array([1.01, 0.5]), iterations=1000)
    j = array([[-500, 100], [201, -100]])
    print part_b(array([.9, .9]), array([1.1, 1.1]), j,  iterations=10000)


if __name__ == "__main__":
    main()
