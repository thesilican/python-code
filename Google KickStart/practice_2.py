import math

testCases = int(input())
for case in range(testCases):
    num = int(input())
    size = math.ceil(num/2)
    l = []
    for c in input():
        l.append(int(c))
    tmp = sum(l[:size])
    mx = tmp
    for i in range(num - size ):
        tmp -= l[i]
        tmp += l[i+size]
        if tmp > mx:
            mx = tmp
    print ("Case #{}: {}".format(case + 1, mx))
