def case(caseNum):
    C, D = [int(x) for x in input().split()]
    lines = [int(x) for x in input().split()]
    computers = []
    for x in range(C - 1):
        arr = [x + 2, -lines[x], None]
        computers.append(arr)
    conn = []
    for x in range(D):
        arr = [int(x) for x in input().split()]
        conn.append(arr)
    computers.sort(key=lambda x: x[1])
    for comp in computers:
        pass
    print("Case #{}: ".format(caseNum))


t = int(input())
for i in range(t):
    case(i + 1)