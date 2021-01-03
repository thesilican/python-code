from timeit import timeit
from util.functions import memoize
from util.primes import isPrime


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n - 2)


@memoize
def fibMem(n):
    print(n)
    if n <= 2:
        return 1
    else:
        return fibMem(n-1) + fibMem(n - 2)


@memoize(pos=0)
def fibMemPos(n):
    if n <= 2:
        return 1
    else:
        return fibMemPos(n-1) + fibMemPos(n - 2)


@memoize(name="n")
def fibMemName(n):
    if n <= 2:
        return 1
    else:
        return fibMemName(n-1) + fibMemName(n - 2)


@memoize(nameKey="n")
def fibMemNameKey(n=1):
    if n <= 2:
        return 1
    else:
        return fibMemNameKey(n=n-1) + fibMemNameKey(n=n-2)


if __name__ == "__main__" and False:
    try:
        print("Normal", fib(10))
        print("Mem", fibMem(100))
        print("Mem Pos", fibMemPos(10))
        print("Mem Name", fibMemName(10))
        print("Mem NameKey", fibMemNameKey(n=10))
        assert fib(10) == fibMem(10)
        assert fib(10) == fibMemPos(10)
        assert fib(10) == fibMemName(10)
        assert fib(10) == fibMemNameKey(n=10)
        amount = "30"
        res = timeit("fib(" + amount + ")", globals=globals(), number=10)
        print(res)
        res = timeit("fibMem(" + amount + ")", globals=globals(), number=10)
        print(res)
    except Exception as e:
        print(e)

# Primes speed test
@memoize
def isPrimeMem(num: int):
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


if __name__ == "__main__":
    res = timeit("[isPrime(x) for x in range(10)]", globals=globals(), number=1000)
    print(res)
    res = timeit("[isPrimeMem(x) for x in range(10)]", globals=globals(), number=1000)
    print(res)
