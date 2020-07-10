# First sort the names into alphabetical order

names = []
with open("problem22.in", "r") as f:
    names = sorted([x[1:-1] for x in f.readline().split(",")])

def nameScore(name, order):
    acc = 0
    for letter in name:
        acc += ord(letter) - ord("A") + 1
    return acc * order

acc = 0
for i, name in enumerate(names):
    score = nameScore(name, i + 1)
    acc += score
print(acc)
