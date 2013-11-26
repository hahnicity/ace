"""
Prove Broyden's method is a solution to

min sigma(sigma((A* - A)^2))

I will show that the equation `A* <- A + (g - Ad)(d'/d'd)` is a solution to the
Frobenius norm outlined above.

    A* <- A + (g - Ad)(d'/d'd) <=> ||A* - A|| = ||(g - Ad)(d'/d'd)|| <=
    ||g - Ad||*||(d'/d'd)|| = ||g - Ad|| * 1 / sigma(xi^2)

We notice that g is subject to s.t. g = A*d

    ||g - Ad|| * 1 / sigma(xi^2) = ||A*d - Ad|| * 1 / sigma(xi^2) <=
    ||A* - A|| * ||d|| * 1 / sigma(xi^2) = ||A* - A||

Thereby showing that ||A* - A|| <= ||(g - Ad)(d'/d'd)||
"""
pass
