"""
Problem 2 from chapter 2

Generate random 100 by 100 matrix A, and 100 vector b solve using assorted algorithms
"""
from functools import wraps
from time import time

from numpy.linalg import inv
from numpy.random import random
from scipy.linalg import lu


def time_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for run_count in [1, 10, 50]:
            start = time()
            func(run_count, *args, **kwargs)
            total = time() - start
            print "For {} each solution took an average of {} to find after {} "\
                  "iterations".format(func.__name__, total / run_count, run_count)
    return wrapper


@time_calls
def part_a(run_count, a, b):
    """
    Solve using inv(A) * b
    """
    for run in xrange(run_count):
        inv(a).dot(b)


@time_calls
def part_b(run_count, a, b):
    """
    Solve using LU decomposition
    """
    _, l, u = lu(a)
    for run in xrange(run_count):
        inv(u).dot(inv(l).dot(b))


@time_calls
def part_c(run_count, a, b):
    """
    Solve using inv(A) * b, but only computing inv(A) once
    """
    a_inverse = inv(a)
    for run in xrange(run_count):
        a_inverse.dot(b)


def main():
    a = random((100, 100))
    b = random((100))
    part_a(a, b)
    part_b(a, b)
    part_c(a, b)


if __name__ == "__main__":
    main()
