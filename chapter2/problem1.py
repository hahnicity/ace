"""
Solve some matrix operations
"""
from numpy import array

from ace.solvers import gauss_jacobi, lu_decomposition


def part_a(a, b):
    """
    Solve using LU decomposition
    """
    print lu_decomposition(a, b)


def part_b(a, b):
    """
    Solve using Gauss-Jacobi
    """
    print gauss_jacobi(a, b, 20, x=[0, 0, 0, 0])


def part_c(a, b):
    """
    Solve using Gauss-Seidel
    """
    pass


if __name__ == "__main__":
    a = array([[54, 14, -11, 2],
               [14, 50, -4, 29],
               [-11, -4, 55, 22],
               [2, 29, 22, 95]])
    b = array([1, 1, 1, 1])
    part_a(a, b)
    part_b(a, b)
