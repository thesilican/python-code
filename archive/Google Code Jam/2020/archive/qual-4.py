def palendrome(arr):
    l = len(arr)
    if (l <= 1):
        return True
    if (arr[0] != arr[l - 1]):
        return False
    return palendrome(arr[1:-1])


def case(b):
    if (b != 10):
        print("You suck")
        exit(b)
    # Ignore first read
    print(1)
    input()
    arr = []
    for i in range(b):
        print(i + 1)
        arr.append(int(input()))
    # print(arr)
    # Poll bits 1
    poll = []
    for i in range(5):
        print(i + 1)
        poll.append(int(input()))
    # Check if palendromic
    if palendrome(arr):
        if poll[0] != arr[0]:
            for i in range(b):
                arr[i] = 1 if arr[i] == 0 else 0
        print("".join(map(str, arr)))
        return
    else:
        if arr[:5] == poll:
            print("".join(map(str, arr)))
            return
        elif arr[5:] == reversed(poll):
            print(reversed("".join(map(str, arr))))
            return
        for i in range(b):
            arr[i] = 1 if arr[i] == 0 else 0
        if arr[:5] == poll:
            print("".join(map(str, arr)))
            return
        elif arr[5:] == reversed(poll):
            print(reversed("".join(map(str, arr))))
            return
        print("0000000000")


inpt = input().split(" ")
t, b = [int(inpt[0]), int(inpt[1])]
for _ in range(t):
    case(b)
    if input() == "N":
        exit(169)