def case(caseNum):
    N, D = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    setA = set(A)
    cuts = 2
    if D == 2:
        if N < 2:
            cuts = 1
        elif len(setA) < N:
            cuts = 0
        else:
            cuts = 1
    elif D == 3:
        skip = False
        if len(A) - len(setA) >= 1:
            d = {}
            for p in A:
                if p not in d:
                    d[p] = 1
                else:
                    d[p] += 1
            doubles = list(filter(lambda x: x[1] > 1, d.items()))
            if len(doubles) >= 1:
                mxDouble = max(doubles, key=lambda x: x[0])
                mx = max(d.items(), key=lambda x: x[0])
                if mx > mxDouble:
                    cuts = 1
                    skip = True
            for k in d:
                if d[k] >= 3:
                    cuts = 0
                    skip = True
        if not skip:
            for p in A:
                for p2 in A:
                    if p == p2 * 2:
                        cuts = 1
                        break
    else:
        print("UwU")
        arr = []
        for i in range(1000000000):
            arr.append("UwU")
        
    print("Case #{}: {}".format(caseNum, cuts))


t = int(input())
for i in range(t):
    case(i + 1)