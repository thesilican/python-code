s = 0
for n in range(1,100_000):
    s += 7**(n-1)/10**n
print(s)