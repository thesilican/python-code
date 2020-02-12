from util.util_numbers import getProperDivisors
from math import copysign

numDict = dict()

acc = 0
for i in range(1, 28123 + 1):
    divSum = sum(getProperDivisors(i))

    found = False
    for j in range(1, i):
        if numDict[j] > 0 and numDict[i - j] > 0:
            found = True
            break
    if not found:
        acc += i
    numDict[i] = divSum - i
print(acc)