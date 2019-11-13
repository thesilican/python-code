import math


def SolveCase(case):
    n, p = [int(x) for x in input().split(" ")]
    total = 0
    for _ in range(n):
        w, h = [int(x) for x in input().split(" ")]
        total += (2 * w) + (2 * h) + (2 * math.sqrt(w**2 + h**2))
    print("Case #{}: {}".format(case, min(p, total)))


numCases = int(input())
for i in range(numCases):
    SolveCase(i + 1)
