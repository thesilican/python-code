from __future__ import print_function
import datetime

MIN = 1
MAX = 12

for num1 in range(MIN, MAX + 1):
    for num2 in range(MIN, MAX + 1):
        inpt = -1
        while inpt != num1 * num2:
            print (str(num1) + " + " + str(num2) + " > ", end="")
            inpt = int(input())
