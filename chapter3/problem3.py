"""
Do some Black-Scholes-Merton fun

Woot! it works!
"""
from math import exp, log, pi, sqrt

from scipy.stats import norm


def make_func(cur_value, strike, tau, rate, delta):
    """
    Create the newton's method function for Black-Scholes
    """
    def regular(d):
        return lambda sigma: (
            cur_value * exp(-delta * tau) * norm.cdf(d(sigma)) -
            strike * exp(-rate * tau) * norm.cdf(d(sigma) - sigma * sqrt(tau))
        )

    def derivative(d):
        return lambda sigma: (
            cur_value * exp(-delta * tau) *
            sqrt(tau / (2 * pi)) * exp(-0.5 * (d(sigma) ** 2))
        )

    # Do some maths to simplify the construction of d
    d = lambda sigma: (
        (log(cur_value / strike) + tau * (rate - delta * .5 * sigma ** 2)) /
        (sigma * sqrt(tau))
    )
    return lambda sigma: (
        sigma - (1 / derivative(d)(sigma)) * regular(d)(sigma)
    )


def newtons(func, sigma, iterations=100):
    for _ in xrange(iterations):
        sigma = func(sigma)
    return sigma


def main():
    # Make up a random option
    cur_value = 20.0
    strike = 27.50
    tau = .33  # Time in years!
    rate = 0.05  # Rate of discount bond
    delta = .01  # dividend rate
    sigma = 1.1
    func = make_func(cur_value, strike, tau, rate, delta)
    print newtons(func, sigma)


if __name__ == "__main__":
    main()
