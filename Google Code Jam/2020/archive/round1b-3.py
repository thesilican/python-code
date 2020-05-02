def solve(R, S):
    for i in range(S - 1):
        a = i * (R-1) + R * (S - i - 1)
        b = (R - 1)
        print(str(a) + " " + str(b))
    if R > 2:
        solve(R - 1, S)

def case(caseNum):
    R, S = [int(x) for x in input().split(" ")]
    l = (S - 1) * (R - 1)
    print("Case #{}: {}".format(caseNum, l))
    solve(R, S)

t = int(input())
for i in range(t):
    case(i + 1)