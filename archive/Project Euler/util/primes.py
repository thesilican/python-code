from math import sqrt, floor
from typing import List
from .functions import memoize


@memoize
def isPrime(num: int) -> bool:
    """Returns True if n is prime.
    Really fast algorithm found online: https://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime"""
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def generatePrimes(upTo: int):
    """Generates all the primes up to a certain number

    Arguments:
        upTo {int} -- The upper limit to check primes up to
    """
    curnum = 2
    while True:
        if isPrime(curnum):
            yield curnum
        if curnum >= upTo:
            return
        curnum += 1


@memoize
def getPrimeFactorization(num: int) -> List[int]:
    if num < 1:
        return getPrimeFactorization(-num) + [-1]
    if num == 0 or num == 1:
        return []

    div = []
    curNum = num
    while(not isPrime(curNum)):
        for i in range(num):
            if isPrime(i) and curNum % i == 0:
                div.append(i)
                curNum = curNum // i
                break
    div.append(curNum)
    return div


@memoize
def getAllDivisors(n: int) -> List[int]:
    """Returns a list of all whole divisors less than n

    For example: 100 -> [1,2,4,5,10,20,25,50]"""
    if (n <= 1):
        return []
    div = [1]
    for i in range(2, floor(sqrt(n))):
        if n % i == 0:
            div.append(i)
            div.append(n//i)
    # Special case for perfect squares
    if n % sqrt(n) == 0:
        div.append(int(sqrt(n)))
    div.sort()
    return div
