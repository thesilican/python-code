import math


def C(n, r):
    return math.factorial(n) / math.factorial(n - r) / math.factorial(r)


def P(n, x, p):
    return C(n, x) * (math.pow(p, x)) * (math.pow(1-p, n-x))


# n = 10
# p = 0.2
# for x in range(0, 11):
#     print(f"{x} - {P(n, x, p)}")
print(P(5, 3, 1/5) + P(5, 4, 1/5) + P(5, 5, 1/5))
