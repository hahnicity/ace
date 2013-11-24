"""
Prove the Gauss-Jacobi method converges for strictly diagonally dominant
matices

We wish to show that the matrix norm representative of the Gauss-Jacobi method,

    ||I - Q^-1*A|| < 1.

Given for Q^-1 in the Gauss-Jacobi Method is the inverse diagonal matrix D

    ||I - Q^-1*A|| = ||I - D^-1*A||

Now we notice that `||I - D^-1*A|| = ||D^-1*R||` where `R` is the remainder
matrix formed by

    A - D = R

It follows that the infinite norm of `D^-1*R` is less than 1

    ||D^-1*R|| < 1

Because the matrix A is strictly diagonally dominant.
"""
pass
