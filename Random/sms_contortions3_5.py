import itertools
numbers = [1,2,3,6,11,20,37,68]
combinations = []
sums = set()
for i in range(4):
    combinations.extend(list(itertools.combinations(numbers, i + 1)))
for i in combinations:
    if 60 <= sum(i) <= 100:
        sums.add(sum(i))
print(sums)