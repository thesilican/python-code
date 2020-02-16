import math


def findPosition(start, end):
    return (end - start + 1)//2

def sortPartition(partitions):
    for i in range(len(partitions)):
        for j in range(len(partitions) - i - 1):
            



t = int(input())
for case in range(0, t + 1):
    splits = input().split()
    n = int(splits[0])
    k = int(splits[1])
    # pos = []
    # for i in range(k):
    #     idealPos = -1
    #     min_ = -1
    #     max_ = -1
    #     for spot in range(n):
    #         if spot in pos:
    #             continue
    #         left = spot
    #         right = n - spot - 1
    #         for p in pos:
    #             if p < spot:
    #                 left = min(spot - p - 1, left)
    #             elif p > spot:
    #                 right = min(p- spot - 1, right)
    #         if idealPos == -1 or min(left, right) > min_ or max(left, right) > max_:
    stalls = [[0, 1]]
    people = [-1 for _ in range(k)]
    for i in range(k):
        pos = findPosition(0, n - 1)

    print(f"Case #{t}:", )
