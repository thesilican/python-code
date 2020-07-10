def case(caseNum):
    N = int(input())
    tasks = []
    for i in range(N):
        inputs = [int(x) for x in input().split(" ")]
        tasks.append(tuple(inputs + [i]))
    tSort = sorted(tasks, key=lambda a: a[0])
    d = {}
    jEnd = -1
    cEnd = -1
    for t in tSort:
        if t[0] >= jEnd:
            d[t[2]] = "J"
            jEnd = t[1]
        elif t[0] >= cEnd:
            d[t[2]] = "C"
            cEnd = t[1]
        else:
            print("Case #{}: IMPOSSIBLE".format(caseNum))
            return

    s = ""
    for i in range(N):
        s += d[i]
    print("Case #{}: {}".format(caseNum, s))


t = int(input())
for i in range(t):
    case(i + 1)
