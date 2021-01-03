import random

zeroToNine = {}
for i in range(10):
    zeroToNine[i] = 0

cache = {}


def getCache(n):
    if n in cache:
        return cache[n]
    d = dict(zeroToNine)
    t = 0
    for i in range(1000):
        M = random.randint(0, n * 10000)
        s = str(M)[:2]
        for c in s:
            d[int(c)] += 1
            t += 1
    for i in range(10):
        d[i] = d[i] / t
    cache[n] = d
    return d


def case(caseNum):
    d = {}
    U = int(input())
    isM = False
    for i in range(10**4):
        inputs = input().split()
        Q = int(inputs[0])
        R = inputs[1]
        for c in R[:2]:
            if Q == -1:
                if c not in d:
                    d[c] = 0
                isM = False
                d[c] += 1
            else:
                if c not in d:
                    d[c] = dict(zeroToNine)
                isM = True
                rCache = getCache(int(str(Q)[:2]))
                for i in range(10):
                    d[c][i] += rCache[i]

    res = ""
    if not isM:
        arr = list(d.items())
        arr.sort(key=lambda x: x[1])
        res = str(arr[0][0]) + "".join(map(lambda x: x[0], reversed(arr[1:])))
    else:
        arr = []
        for i in list(range(1, 10)) + [0]:
            c = ""
            mx = -1
            for k in d:
                nums = list(d[k].items())
                score = nums[i][1]
                if score > mx:
                    mx = score
                    c = k
            arr.append(c)
            del d[c]
        arr.insert(0, arr.pop())
        res = "".join(map(lambda x: x[0], arr))
    print("Case #{}: {}".format(caseNum, res))


t = int(input())
for i in range(t):
    case(i + 1)
