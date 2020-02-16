def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(sort([4,2,6,7,1,2,2,2]))