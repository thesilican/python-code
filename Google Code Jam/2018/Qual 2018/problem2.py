def TroubleSort(L: list) -> list:
    finished = False
    while not finished:
        finished = True
        for i in range(len(L) - 2):
            if L[i] > L[i+2]:
                finished = False
                temp = L[i]
                L[i] = L[i+2]
                L[i+2] = temp


def SolveCase(case):
    input()
    L = [int(x) for x in input().split(" ")]
    TroubleSort(L)
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            print("Case #{}: {}".format(case, i))
            return
    print("Case #{}: OK".format(case))


numCases = int(input())
for i in range(numCases):
    SolveCase(i + 1)
