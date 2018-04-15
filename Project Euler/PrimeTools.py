from math import sqrt; from itertools import count, islice


"""
Lol I basically stole this from
https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
"""
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))