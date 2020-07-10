from util.primes import generatePrimes, isPrime, getPrimeFactorization, getAllDivisors

if __name__ == "__main__":
    assert isPrime(9223372036854775807) == False
    assert isPrime(9223372036854775807) == False
    assert getPrimeFactorization(1) == []
    assert getPrimeFactorization(-5) == [5, -1]
    assert getPrimeFactorization(101) == [101]
    assert getPrimeFactorization(123456789) == [3, 3, 3607, 3803]
    assert getPrimeFactorization(9223372036854775807) == [
        7, 7, 73, 127, 337, 92737, 649657]
    assert getPrimeFactorization(89809353444902571) == [3, 3, 9978817049433619]
    assert getAllDivisors(100) == [1, 2, 4, 5, 10, 20, 25, 50]
