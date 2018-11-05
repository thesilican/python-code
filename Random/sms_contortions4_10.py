from itertools import combinations

for a, b, c in combinations(range(1,17), 3):
    if a != b and b != c and a != c and \
        a + b + c < 17 and \
        a < b + c and b < a + c and c < a + b:
        print(f"{a}, {b}, {c}")