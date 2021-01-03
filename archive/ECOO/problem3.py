def OCR():
    H, W = [int(x) for x in input().split()]
    rows = []
    for _ in range(H):
        inpt = input()
        n = []
        for i, s in enumerate(inpt):
            if s == "*":
                n.append(i)
        rows.append(n)
    while True:
        if len(rows[0]) != 0:
            break
        rows.pop(0)
    while True:
        if len(rows[-1]) != 0:
            break
        rows.pop()
    # Time for Ad-hoc
    if len(rows) % 2 == 0:
        return 7
    mid = (len(rows) - 1) // 2
    if len(rows[mid]) == 0:
        # 0 or 1
        if len(rows[mid + 1]) == 1:
            return 1
        else:
            return 0
    if len(rows[mid - 1]) == 2:
        if len(rows[mid + 1]) == 2:
            return 8
        else:
            if len(rows) == 3 or rows[0] == rows[1]:
                return 4
            else:
                return 9
    else:
        if len(rows[mid + 1]) == 2:
            return 6
        if rows[mid - 1] == rows[mid + 1]:
            return 3
        if rows[mid - 1] > rows[mid + 1]:
            return 2
        if rows[mid - 1] < rows[mid + 1]:
            return 5


def case():
    N = int(input())
    s = []
    for _ in range(N):
        s.append(str(OCR()))
    print("".join(s))


T = int(input())
for i in range(T):
    case()
