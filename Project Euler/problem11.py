array = []

file = open("./problem11.in", "r")
for line in file:
    x = line.rstrip("\n").split(" ")
    a = []
    for n in x:
        a.append(int(n))
    array.append(a)

# Horizontal search
mx = 0
loc = [-1, -1]
direction = ""
for i in range(len(array)):
    row = array[i]
    for j in range(len(row) - 3):
        prod = row[j] * row[j + 1] * row[j + 2] * row[j + 3]
        if prod > mx:
            mx = prod
            loc = [i, j]
            direction = "Right"

# Vertical search
for i in range(len(array) - 3):
    for j in range(len(row)):
        prod = array[i][j] * array[i + 1][j] * \
            array[i + 2][j] * array[i+3][j]
        if prod > mx:
            mx = prod
            loc = [i, j]
            direction = "Down"

# Diagonal searches
for i in range(len(array) - 3):
    for j in range(len(row) - 3):
        prod = array[i][j] * array[i + 1][j + 1] * \
            array[i + 2][j + 2] * array[i+3][j + 3]
        if prod > mx:
            mx = prod
            loc = [i, j]
            direction = "Down Right"

for i in range(len(array) - 3):
    for j in range(3, len(row)):
        print (i, j)
        prod = array[i][j] * array[i + 1][j - 1] * \
            array[i + 2][j - 2] * array[i+3][j - 3]
        if prod > mx:
            mx = prod
            loc = [i, j]
            direction = "Down Left"

print(mx, loc, direction)
