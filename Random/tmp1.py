import itertools
import collections
import functools

arr = [x for x in range(1, 100 + 1)]
perms = itertools.combinations(arr, 12)
print("Starting...")
print(len(list(perms)))

def ver(arr):
    print(arr)
    total = sum(map(lambda x: 1 if 15 <= x <= 40 else 0, arr))
    if total >= 10:
        return True
    return False

print(len(list(filter(ver, arr))))
