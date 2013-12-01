"""
Solve the complementarity problem

I  had a lot of difficulty with this because I was looking for a solution
for the constraint equation

    sigma(pj * xij) = sigma(pj * eij)

This was a dead end due to the face we cannot create a square matrix from the
variables involved. Thus we cannot implement a root finding solution

I wish I could figure this out, but I can't
"""
from numpy import array, maximum, minimum


def simulate_economy(a, v, e, iterations=100):
    for i in xrange(2):
        for _ in xrange(iterations):
            f = "foo"
            fhat = minimum(maximum())

def main():
    simulate_economy(a, v, e)

if __name__ == "__main__":
    main()
