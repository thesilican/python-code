def printOut():
    halfLen = int(len(inpts)/2)
    A = inpts[:halfLen]
    B = inpts[halfLen:]
    for i in range(halfLen):
        print(A[halfLen - i - 1], end=" ")
        print(B[i], end = " ")

input()
inpts = input().split(" ")
inpts = [int(x) for x in inpts]
inpts.sort()
if len(inpts) % 2 == 0:
    printOut()
else:
    first = inpts.pop(0)
    printOut()
    print(first)
