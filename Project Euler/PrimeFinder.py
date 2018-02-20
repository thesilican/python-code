import math

def getPrimes(maximum):
    global __primes
    if maximum not in __primes:
        __primes = list(range(1,maximum + 1))
        # Of course 1 isn't prime
        __primes.remove(1)
        currentNum = 2
        sqrtMax = math.sqrt(math.ceil(maximum))
        while currentNum < sqrtMax:
            print("Trying " + str(currentNum))
            if currentNum in __primes:
                index = 0
                while index < len(__primes):
                    if __primes[index] % currentNum == 0 and __primes[index] != currentNum:
                        # print("\tRemoving " + str(__primes[index]) + " from list!")
                        del __primes[index]
                    index += 1
            currentNum += 1
    return __primes


__primes = []
if __name__ is "__main__":
    print("Get all prime numbers up to: ", end=" ")
    times = int(input())
    print(getPrimes(times))