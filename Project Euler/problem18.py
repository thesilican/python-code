# Oh well may as well brute force
tree = []

# Load tree
file = open("./problem18.in", "r")
for line in file:
  nums = line.rstrip("\n").split(" ")
  tree.append([int(x) for x in nums])

# Recursive function to navigate tree
maxDepth = len(tree)
def recurseMaxSum(x=0, y=0, curSum=0):
  if y == maxDepth - 1:
    return curSum + tree[y][x]
  else:
    option1 = recurseMaxSum(x, y+1, curSum)
    option2 = recurseMaxSum(x+1, y+1, curSum)
    return max(option1, option2) + tree[y][x]

if __name__ == "__main__":
    print(recurseMaxSum())