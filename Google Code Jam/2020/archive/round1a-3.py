def calcInterest(dancers):
    return sum([sum([y for y in x if y != None]) for x in dancers])


def buildAvgs(dancers, R, C):
    # Generate a table of averages
    avgs = [[[] for _ in range(C)] for _ in range(R)]
    # Sweep over rows
    for i in range(R):
        cur = -1
        # Forwards
        for j in range(C):
            num = dancers[i][j]
            if num != None:
                if cur != -1:
                    avgs[i][j].append(cur)
                cur = num

        # Backwards
        cur = -1
        for j in range(C - 1, -1, -1):
            num = dancers[i][j]
            if num != None:
                if cur != -1:
                    avgs[i][j].append(cur)
                cur = num

    # Sweep over columns
    for j in range(C):
        cur = -1
        # Forwards
        for i in range(R):
            num = dancers[i][j]
            if num != None:
                if cur != -1:
                    avgs[i][j].append(cur)
                cur = num
        # Backwards
        cur = -1
        for i in range(R - 1, -1, -1):
            num = dancers[i][j]
            if num != None:
                if cur != -1:
                    avgs[i][j].append(cur)
                cur = num
    return [[(sum(x) / len(x) if len(x) > 0 else None) for x in y] for y in avgs]


def case(caseNum):
    R, C = [int(x) for x in input().split()]

    dancers = []
    for i in range(R):
        dancers.append([int(x) for x in input().split()])

    # Big loop, eliminating every round
    interest = 0
    numChange = -1
    while numChange != 0:
        interest += calcInterest(dancers)
        avgs = buildAvgs(dancers, R, C)

        # Remove if below average
        numChange = 0
        for i in range(R):
            for j in range(C):
                dancer = dancers[i][j]
                avg = avgs[i][j]
                if dancer == None or avg == None:
                    continue
                if dancer < avgs[i][j]:
                    dancers[i][j] = None
                    numChange += 1

    print("Case #{}: {}".format(caseNum, interest))

t = int(input())
for i in range(t):
    case(i + 1)
