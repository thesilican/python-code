def case(caseNum):
    L, R = [int(x) for x in input().split()]
    n = 1
    while True:
        if R > L:
            if n > R:
                break
            R -= n
        else:
            if n > L:
                break
            L -= n
        n += 1
    print("Case #{}: {} {} {}".format(caseNum, n - 1, L, R))


t = int(input())
for i in range(t):
    case(i + 1)