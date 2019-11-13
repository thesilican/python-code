CHARS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def GenPrimes(UpTo):
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    try:
        while q <= UpTo:
            if q not in D:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                yield q
                D[q * q] = [q]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next 
                # multiples of its witnesses to prepare for larger
                # numbers
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            
            q += 1
    except GeneratorExit:
        return

def isPrime(num: int):
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

for i in range(100):
    GenPrimes(10000)

t = int(input())
for case in range(t):
    n, l = [int(x) for x in input().split(" ")]
    nums = [int(x) for x in input().split(" ")]

    firstNumsSwapped = []
    outputNums = []    
    # Decrypt first number
    for p in GenPrimes(n):
        if (nums[0] / p).is_integer():
            outputNums.append(p)
            outputNums.append(int(nums[0] / p))
            firstNumsSwapped.append(int(nums[0] / p))
            firstNumsSwapped.append(p)
            break
    
    # Decrypt all the nums - swap the first/second value if
    # you run into an invalid state
    while True:
        breakLoop = True
        for i in range(1,l):
            newNum = nums[i] / outputNums[i]
            if not newNum.is_integer():
                breakLoop = False
                break
            outputNums.append(int(newNum))
        
        if breakLoop:
            break
        outputNums = list(firstNumsSwapped)

    
    charNum = sorted(set(outputNums))
    assert len(charNum) == 26
    charDict = {}
    for i in range(26):
        charDict[charNum[i]] = CHARS[i]

    outStr = ""
    for i in outputNums:
        outStr += charDict[i]

    # Decrypt the numbers to letters
    print ("Case #" + str(case + 1) + ": " + outStr)