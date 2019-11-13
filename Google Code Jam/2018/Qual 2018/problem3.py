def SolveCase(case):
    # Hard-coding the answer :P
    # I'm only going to go for the small case
    input()
    squares = [[0 for i in range(5)] for i in range(4)]
    coords = [[1, 1], [2, 1], [1, 3], [2, 3]]
    while True:
        ccounts = [0, 0, 0, 0]
        for c in range(4):
            for i in range(3):
                for j in range(3):
                    if squares[i - 1 + coords[c][0]][j - 1 + coords[c][1]] == 0:
                        ccounts[c] += 1
        send = ccounts.index(max(ccounts))
        print("{} {}".format(coords[send][0] + 10, coords[send][1] + 10))

        x, y = [int(x) for x in input().split(" ")]
        if (x == y == 0):
            return
        elif (x == y == -1):
            exit()
        else:
            squares[x - 10][y - 10] = 1


numCases = int(input())
for i in range(numCases):
    SolveCase(i + 1)
