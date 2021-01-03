def case(case):
    n = int(input())
    rows = [{} for _ in range(n)]
    rowCheck = [False for _ in range(n)]
    cols = [{} for _ in range(n)]
    colCheck = [False for _ in range(n)]
    acc = 0
    for i in range(n):
        splits = [int(x) for x in input().split(" ")]
        for j in range(n):
            l = splits[j]
            if rowCheck[i]:
                pass
            elif l in rows[i]:
                rowCheck[i] = True
            else:
                rows[i][l] = True
            if colCheck[j]:
                pass
            elif l in cols[j]:
                colCheck[j] = True
            else:
                cols[j][l] = True
            if i == j:
                acc += l
    c = 0
    for i in colCheck:
        if i:
            c += 1
    r = 0
    for i in rowCheck:
        if i:
            r+= 1
    # print (rowCheck, colCheck, acc)

    print("Case #{}: {} {} {}".format(case, acc, r, c))


t = int(input())
for i in range(t):
    case(i + 1)
