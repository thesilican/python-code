def getNext(num, div):
    while num < div:
        num *= 10
    return num % div


def getLen(div):
    num = 1
    d = {}
    while num not in d:
        d[num] = getNext(num, div)
        if d[num] == 0:
            # No repeats
            return 0
        num = d[num]

    # Get loop length
    counter = 1
    orig = num
    num = d[num]
    while num != orig:
        counter += 1
        num = d[num]
    return counter


mx = 0
for i in range(1, 1000):
    l = getLen(i)
    if l > mx:
        mx = l
        print(i, "-", l)
