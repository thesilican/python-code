def bubbleSort(arr):
    l = len(arr)
    for i in range(l):
        for j in range(l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


if __name__ == "__main__":
    arr = [0, 8, 2, 3, 1, 5, 4, 7, 6, 9]
    bubbleSort(arr)
    print(arr)
