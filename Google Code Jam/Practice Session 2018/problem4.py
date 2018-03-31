def AddPerson(stalls: list):
    max_ = 0
    index = -1
    for i in range(len(stalls)):
        if stalls[i] > max_:
            max_ = stalls[i]
            index = i
    num = stalls.pop(i)
    x = y = 0
    if num % 2 == 0:
        x = num / 2 - 1
        y = num / 2
    else:
        x = y = (num-1)/2
    stalls.insert(index, x)
    stalls.insert(index + 1, y)
    return stalls


def SolveCase(case):
    n, k = [int(x) for x in input().split(" ")]
    stalls = [n]
    for _ in range(k - 1):
        AddPerson(stalls)
    # Ctrl-C Ctrl-V!
    max_ = 0
    index = -1
    for i in range(len(stalls)):
        if stalls[i] > max_:
            max_ = stalls[i]
            index = i
    num = stalls.pop(i)
    x = y = 0
    if num % 2 == 0:
        x = num / 2 - 1
        y = num / 2
    else:
        x = y = (num-1)/2
    print("Case #{}: {} {}".format(case, int(max(x, y)), int(min(x, y))))


numCases = int(input())
for i in range(numCases):
    SolveCase(i + 1)
