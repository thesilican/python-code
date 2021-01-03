import math
n = int(input())
data = []
for _ in range(n):
    splits = [int(x) for x in input().split()]
    data.append(splits)


def merge(arr, low, mid, high):
    arrCopy = arr[:]
    ptr = low
    lPtr = low
    hPtr = mid + 1
    while lPtr <= mid and hPtr <= high:
        if arrCopy[lPtr] < arrCopy[hPtr]:
            arr[ptr] = arrCopy[lPtr]
            lPtr += 1
        else:
            arr[ptr] = arrCopy[hPtr]
            hPtr += 1
        ptr += 1

    while lPtr <= mid:
        arr[ptr] = arrCopy[lPtr]
        lPtr += 1
        ptr += 1
    while hPtr <= high:
        arr[ptr] = arrCopy[hPtr]
        hPtr += 1
        ptr += 1


def sortArr(arr, low, high):
    if low == high:
        return
    if high - low == 1:
        if arr[high] < arr[low]:
            arr[high], arr[low] = arr[low], arr[high]
        return
    pivot = low + math.floor((high - low) // 2)
    sortArr(arr, low, pivot)
    sortArr(arr, pivot + 1, high)

    merge(arr, low, pivot, high)


sortArr(data, 0, len(data) - 1)
maxSpeed = 0

for i in range(len(data) - 1):
    time = data[i + 1][0] - data[i][0]
    dist = abs(data[i + 1][1] - data[i][1])
    speed = dist/time
    if speed > maxSpeed:
        maxSpeed = speed

print(maxSpeed)
