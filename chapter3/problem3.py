"""
Do some Black-Scholes-Merton fun
"""
from math import exp, log, pi, sqrt

from scipy.stats import norm


def make_func(cur_value, strike, tau, rate, delta):
    """
    """
    def regular(d):
        return lambda sigma: (
            cur_value * exp(-delta * tau) * norm.cdf(d(sigma)) -
            strike * exp(-rate * tau) * norm.cdf(d(sigma) - sigma * sqrt(tau))
        )

    def derivative(d):
        return lambda sigma: (
            cur_value * exp(-delta * tau) *
            sqrt((tau / (2 * pi)) * exp(-0.5 * (d(sigma) ** 2)))
        )

    d = lambda sigma: (
        ((log(cur_value * exp(-delta * tau)) - log(strike * exp(-rate * tau))) /
         sigma * sqrt(tau)) + (0.5 * sigma * sqrt(tau))
    )
    return lambda sigma: (
        sigma - (1 / derivative(d)(sigma)) * regular(d)(sigma)
    )


def newtons(func, sigma, iterations=100):
    for _ in xrange(iterations):
        sigma = func(sigma)
    return sigma


def main():
    cur_value = 20
    strike = 7.50
    tau = 60
    rate = 0.01
    delta = .01
    sigma = .1
    d = lambda sigma: (
        ((log(cur_value * exp(-delta * tau)) - log(strike * exp(-rate * tau))) /
         sigma * sqrt(tau)) + (0.5 * sigma * sqrt(tau))
    )
    print d(sigma), d(sigma) ** 2, -0.5 * d(sigma) ** 2
    print ((tau / (2 * pi)) * exp(-0.5 * d(sigma) ** 2))
    print sqrt((tau / (2 * pi)) * exp(-0.5 * d(sigma) ** 2))
    func = make_func(cur_value, strike, tau, rate, delta)
    print newtons(func, sigma)


if __name__ == "__main__":
    main()
