import math

def isPrime(n):
    if n <= 1 or n == 4:
        return False
    if n == 2 or n == 3 or n == 5:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

tests = int(input())
for _ in range(tests):
    num = int(input())
    if isPrime(num):
        print(f"{num} {num}")
        continue
    for i in range(10000):
        ch = i + 1
        if isPrime(num + ch) and isPrime(num - ch):
            print(str(num + i + 1) + " " + str(num - (i + 1)))
            break