from math import sqrt, floor
from itertools import count, islice
from typing import List

_primeDict = {}
def isPrime(n: int, store: bool = True) -> bool:
    """Finds out if a number is prime DUH. Also stores numbers already proved to be prime"""
    def _isPrime(num: int):
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
    
    if store and n in _primeDict:
        return _primeDict[n]
    numIsPrime = _isPrime(n)
    _primeDict[n] = numIsPrime
    return numIsPrime

def getPrimeDivisors(n: int, debug: bool = False ) -> List[int]:

    def log(*args):
        if debug:
            print(" ".join(map(lambda x: str(x), args)))
    log("Prime factoring", n)
    div = []
    curNum = n
    while(not isPrime(curNum)):
        log("Finding prime factors of", curNum)
        for i in range(n):
            if isPrime(i) and curNum % i == 0:
                log("   Found a prime factor:", i)
                div.append(i)
                curNum = curNum // i
                break
    div.append(curNum)
    log("Remaining number", curNum, "is prime")
    return div
                
def getAllDivisors(n: int, debug: bool = False) -> List[int]:
    """Returns a list of all whole divisors less than n

    For example: 100 -> [1,2,3,4,5,10,20,25,50]"""
    # Naive approach once again...
    # Once I get better at math I'll fix this
    if (n <= 1):
        return []
    div = []
    for i in range(2, floor(sqrt(n))):
        if n % i == 0:
            div.append(i)
            div.append(n//i)
    div.append(1)
    return sorted(div)
        

if __name__ == "__main__":
    print(isPrime(9223372036854775807))
    print(isPrime(9223372036854775807))
    print(getPrimeDivisors(123456789, True))
    print(getPrimeDivisors(9223372036854775807, True))
    print(getPrimeDivisors(89809353444902571, True))