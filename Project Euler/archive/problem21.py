from util.numbers import getDivisors

amical = []
for i in range(2, 10001):
    factors = getDivisors(i)
    factors.remove(i)
    amicalNum = sum(factors)
    amicalFactors = getDivisors(amicalNum)
    amicalFactors.remove(amicalNum)
    amicalAmicalNum = sum(amicalFactors)
    print(amicalAmicalNum == i, i, amicalNum, amicalAmicalNum)
    
    if (amicalAmicalNum == i and amicalNum != i):
        amical.append(i)

print(getDivisors(220))
print(amical)
print(sum(amical))