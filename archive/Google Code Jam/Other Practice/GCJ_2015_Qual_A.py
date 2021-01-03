import math
def SolveCase(inputStr):
    inputs = inputStr.split(' ')
    cases = inputs[0]
    shynesses = list(inputs[1].strip())

    minNeeded = 0
    for i in range(len(shynesses)):
        sumOfPreviousPeople = sum(map(int,shynesses[:i]))
        if sumOfPreviousPeople < i:
            minNeeded = max(i - sumOfPreviousPeople, minNeeded)
    return str(minNeeded)