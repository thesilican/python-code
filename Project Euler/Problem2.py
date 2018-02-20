fibs = [1,1]
while(fibs[-1] < 4_000_000):
    fibs.append(fibs[-1] + fibs[-2])
sums = 0
for s in fibs:
    if s % 2 == 0:
        sums += s
print(sums)