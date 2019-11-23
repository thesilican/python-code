import string


def IsMajority(parties):
    max_ = 0
    sum_ = 0
    for i in parties:
        if i > max_:
            max_ = i
        sum_ += i
    if max_ > (sum_ / 2):
        return True
    return False


def Biggest(parties):
    maxnum = 0
    maxindex = -1
    for i in range(len(parties)):
        if parties[i] > maxnum:
            maxindex = i
            maxnum = parties[i]
    return maxindex


def SolveCase(case):
    input()
    parties = [int(x) for x in input().split(" ")]
    output = "Case #" + str(case) + ":"
    while True:
        output += " "
        if (parties[Biggest(parties)] == 0):
            break
        output += string.ascii_uppercase[Biggest(parties)]
        parties[Biggest(parties)] -= 1
        if IsMajority(parties):
            output += string.ascii_uppercase[Biggest(parties)]
            parties[Biggest(parties)] -= 1
    print(output)


numCases = int(input())
for i in range(numCases):
    SolveCase(i + 1)
