"""
Solve matrix multiplication of

    [[0, -1, 2],    [[-7, 1, 1],
C =  [-2, -1, 4], *  [7, -3, -2],
     [2, 7, -2]]     [3, 5, 0]]

a. Solve Cx = [3, -1, 2],

Then do a bunch of other stuff that I don't want to write off
because doing work in ASCII characters is a pain
"""
from numpy import array, linalg

A = array([[0, -1, 2], [-2, -1, 4], [2, 7, -2]])
B = array([[-7, 1, 1], [7, -3, -2], [3, 5, 0]])
y = array([3, -1, 2])


def part_a():
    """
    Solve Cx = y using standard matrix multiplication for A and B
    """
    C = A.dot(B)
    x = linalg.solve(C, y)
    return x


def part_b():
    """
    Solve Cx = y using element-wise multiplication (Hadamard product)
    """
    C = A * B
    x = linalg.solve(C, y)
    return x


def main():
    print "Matrix multiplication"
    print part_a()
    print "\nElement-wise multiplication"
    print part_b()


if __name__ == "__main__":
    main()
