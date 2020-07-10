d = {}
def nextNum(n):
    if n in d:
        return d[n]
    if n % 2 == 0:
        d[n] = n // 2
        return n // 2
    else:
        d[n] = 3 * n + 1
        return 3 * n + 1

def collatz(n):
    arr = [n]
    while True:
        if arr[-1] == 1:
            return arr
        arr.append(nextNum(arr[-1]))

if __name__ == "__main__":
    print(collatz(9))
