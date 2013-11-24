"""
Solve a more complex newtons method

f(x) = (x+1)^2 - (1+c^2)

where 1+c^2 > 0 <=> c > sqrt(-1) which for our purposes means we
are guaranteed for all c some solution.
"""


def newtons(func, x, iterations=100):
    for _ in xrange(iterations):
        x = func(x)
    return x


def make_fx(c):
    return lambda x: (
        x - (1.0 / (2.0 * x + 2.0)) *
        ((x + 1) ** 2 - (1 + c ** 2))
    )


def part_a():
    make_fx(1)


def part_b():
    """
    So I'm changing my opinion on this part. Given that we are using
    a parabolic equation we will always have 2 roots. It is sufficient
    in this case to make a guess about where we think f(x)=0 but we
    also must consider that we must take into account the other root
    thus we should pick a point on the curve where f'(x) > 0 and f'(x) < 0
    and search for our roots in both places. It is sufficient that we
    can reuse the values we chose here.
    """
    pass


def part_c():
    for c in xrange(-50, 50):
        fx = make_fx(c)
        pos_start = 0
        neg_start = -2
        print newtons(fx, pos_start), newtons(fx, neg_start)


def main():
    part_c()


if __name__ == "__main__":
    main()
