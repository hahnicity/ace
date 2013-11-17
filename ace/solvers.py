"""
ace.solvers
~~~~~~~~~~~

Solve a simple linear equation Ax = b in a particular way
"""
from numpy import append, array, diagonal, tril, triu
from numpy.linalg import inv, solve
from scipy.linalg import lu


def lu_decomposition(a, b):
    """
    Solve a linear equation by LU-decomposition

    Comes from LU decomposition of a matrix A s.t. A = LU

    Then

        LUx = b => Ux = y => Ly = b
    """
    _, l, u = lu(a)
    y = solve(l, b)
    return solve(u, y)


def gauss_seidel(a, b, iterations, x=None):
    """
    Solve a linear equation by the gauss seidel iteration outlined in the book

    Follows the eq:

        x = inv(L)*(b - U*x)
    """
    l = tril(a)
    upper_plus_diagonal = triu(a)
    u = upper_plus_diagonal - _diagonal_matrix(a)
    x = _check_for_initial_guess(a, x)
    for _ in xrange(iterations):
        x = inv(l).dot(b - u.dot(x))
    return x


def gauss_jacobi(a, b, iterations, x=None):
    """
    Solve a linear equation by the gauss jacobi iteration outlined in the book.

    Follows the eq:

        x = inv(D)(b - Rx)

    Where D is the diagonal matrix of A and R is the remainder s.t D + R = A
    """
    d = _diagonal_matrix(a)
    # Calculate the remainder matrix
    r = a - d
    x = _check_for_initial_guess(a, x)
    for _ in xrange(iterations):
        x = inv(d).dot(b - r.dot(x))
    return x


def _diagonal_matrix(a):
    """
    Given a square, 2D matrix a, create a diagonal matrix from it
    """
    diag = diagonal(a)
    # Create first row to initialize the correct shape
    first_row = [diag[0]] + [0 for _ in range(len(diag) - 1)]
    diag_matrix = array([first_row])
    # Construct the remaining rows in the diagonal matrix
    for index in range(1, len(diag)):
        row = [0 if index != i else diag[i] for i in range(len(diag))]
        diag_matrix = append(diag_matrix, [row], axis=0)
    return diag_matrix


def _check_for_initial_guess(a, x):
    """
    If we have not provided an initial array for x make a new one
    """
    if not x:
        x = array([1 for _ in range(a.shape[1])])
    return x
