def a(n):
    return 1/(n+1)**2

def b(n):
    return (n*(n+1)/2)**2

s = sum(a(n) * b(n) for n in range(1, 51 + 1))
print(s)