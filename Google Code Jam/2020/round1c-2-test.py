import random

d = {}
t = 0
for i in range(10):
    d[i] = 0

for i in range(10_000):
    U = random.randint(0, 10**2)
    M = random.randint(0, U)
    s = str(M)[:2]
    for c in s:
        d[int(c)] += 1
        t += 1

for c in d:
    print(d[c] / t)
