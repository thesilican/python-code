# Oh well may as well brute force
tree = []

file = open("./problem18.in", "r")
for line in file:
  nums = line.rstrip("\n").split(" ")
  tree.append([int(x) for x in nums])

