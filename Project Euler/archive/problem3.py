import math
from util.util_primes import isPrime
number = 600851475143
sqrtNum = math.ceil(math.sqrt(number))

highestPrime = 0
for i in range(1,sqrtNum + 1):
    if(number % i == 0 and isPrime(i)):
        highestPrime = i
print(highestPrime)