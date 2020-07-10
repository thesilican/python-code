import math
from typing import List
from functools import reduce

store = {}

def factors(n):
    n = int(n)
    if n in store:
        return store[n]
    for f in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % f == 0:
            store[n] = [f] + factors(n / f)
            return store[n]
    store[n] = [n]
    return store[n]


def GCF(a: List[int], b: List[int]):
    fs = [1]
    f1 = factors(a)
    f2 = factors(b)
    p1 = 0
    p2 = 0
    while p1 < len(f1) and p2 < len(f2):
        if f1[p1] == f2[p2]:
            fs.append(f1[p1])
            f1.pop(p1)
            f2.pop(p2)
        elif f1[p1] > f1[p2]:
            p2 += 1
        else:
            p1 += 1
    return reduce(lambda x, y: x * y, fs)

def betterGCF(a, b):
    return a if b == 0 else betterGCF(b, a%b)

mx = 0
for n in range(1, 10_000_000):
    val = betterGCF(100 + (n ** 2), 100 + ((n +1) ** 2))
    if val > mx:
        mx = val
print(mx)