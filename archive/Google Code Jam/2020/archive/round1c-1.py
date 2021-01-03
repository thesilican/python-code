import math


def case(caseNum):
    inputs = input().split()
    X = int(inputs[0])
    Y = int(inputs[1])
    S = inputs[2]

    sol = -1
    for i, c in enumerate(S):
        if c == "N":
            Y += 1
        elif c == "S":
            Y -= 1
        elif c == "E":
            X += 1
        elif c == "W":
            X -= 1
        if abs(X) + abs(Y) <= i + 1:
            sol = i + 1
            break

    print("Case #{}: {}".format(caseNum, "IMPOSSIBLE" if sol == -1 else sol))


t = int(input())
for i in range(t):
    case(i + 1)
