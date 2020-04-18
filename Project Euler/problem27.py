from util.util_primes import isPrime

# Try all
mx = 0
aMx = 0
bMx = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while isPrime((n ** 2) + (a * n) + b):
            n += 1
        if n > mx:
            mx = n
            aMx = a
            bMx = b
print(mx, aMx, bMx)
