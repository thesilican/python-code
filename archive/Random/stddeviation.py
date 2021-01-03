import math

def stddeviation(arr):
    n = len(arr)
    avg = sum(arr)/n
    sqr = sum(map(lambda x: (x-avg)**2,arr))
    return math.sqrt(sqr/(n - 1))

arr = [1,2,3,4,5]
print(stddeviation(arr))
