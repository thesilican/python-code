def s(p):
    a = p
    d = 2*p-1
    n = 40
    return n*(2 * a + (n-1) * d)//2

print(
    sum([s(n) for n in range(1, 10 + 1)])
)