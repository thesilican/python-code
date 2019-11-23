import math


def SolveCase():
    # Min is exclusive Min is inclusive
    min, max = [int(x) for x in input().split(" ")]
    maxCases = int(input())
    for i in range(maxCases):
        guess = math.ceil((min + max) / 2)
        print(guess)
        response = input()
        if response == "CORRECT":
            break
        elif response == "TOO_BIG":
            max = guess - 1
        elif response == "TOO_SMALL":
            min = guess
        else:
            break


numCases = int(input())
for i in range(numCases):
    SolveCase()
