from typing import List


def case(caseNum):
    N = int(input()) - 1
    sol: List[str] = ["1 1"]

    i = 2
    while N - (i - 1) >= 0:
        N -= (i - 1)
        sol.append(str(i) + " 2")
        i += 1

    i -= 1
    for _ in range(N):
        sol.append(str(i) + " 1")
        i += 1

    print("Case #{}:\n{}".format(caseNum, "\n".join(sol)))


t = int(input())
for i in range(t):
    case(i + 1)
