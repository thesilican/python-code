import math

numTests = int(input())
for _ in range(numTests):
    splits = input().split()
    n = input()
    a, b = int(splits[0]), int(splits[1])
    while True:
        guess = round((a+b)/2)
        print(guess)
        response = input()
        if response == "CORRECT":
            break
        elif response == "TOO_SMALL":
            a = guess
        elif response == "TOO_BIG":
            b = guess
        else:
            exit()