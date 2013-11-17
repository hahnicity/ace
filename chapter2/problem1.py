"""
Solve some matrix operations
"""
from numpy import array

from ace.solvers import gauss_jacobi, gauss_seidel, lu_decomposition


def part_a(a, b):
    """
    Solve using LU decomposition
    """
    x = lu_decomposition(a, b)
    print x
    return x


def part_b(a, b, x_exact):
    """
    Solve using Gauss-Jacobi
    """
    for iterations in xrange(1, 100):
        x = gauss_jacobi(a, b, iterations)
        if _check_for_significant_digits(x, x_exact, 4):
            print iterations, x
            return


def part_c(a, b, x_exact):
    """
    Solve using Gauss-Seidel
    """
    for iterations in xrange(1, 100):
        x = gauss_seidel(a, b, iterations)
        if _check_for_significant_digits(x, x_exact, 4):
            print iterations, x
            return


def _check_for_significant_digits(x, x_exact, desired_digits):
    number_validated = 0
    for i, xi in enumerate(x_exact):
        comparator = int(xi * 10 ** desired_digits)
        if int(x[i] * 10 ** desired_digits) == comparator:
            number_validated += 1
    if number_validated == len(x_exact):
        return True
    return False


if __name__ == "__main__":
    a = array([[54, 14, -11, 2],
               [14, 50, -4, 29],
               [-11, -4, 55, 22],
               [2, 29, 22, 95]])
    b = array([1, 1, 1, 1])
    x_exact = part_a(a, b)
    part_b(a, b, x_exact)
    part_c(a, b, x_exact)
