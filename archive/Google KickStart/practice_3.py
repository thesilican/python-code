# Too hard, admit defeat

testCases = int(input())
for testCase in range(testCases):
    N, K, x1, y1, C, D, E1, E2, F = [int(x) for x in input().split()]
    A = []
    xNext = x1
    yNext = y1
    A.append((x1+y1) % F)
    for i in range(N - 1):
        xNextOrg = xNext
        yNextOrg = yNext
        xNext = (C*xNextOrg + D*yNextOrg + E1) % F
        yNext = (D*xNextOrg + C* yNextOrg + E2) % F
        A.append((xNext + yNext) % F)
    