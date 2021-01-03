import itertools

needle = input()
haystack = input()

searchLen = len(haystack) - len(needle) + 1
needleLen = len(needle)

t = set(itertools.permutations(needle))
perms = ["".join(x) for x in t]

count = 0
for search in perms:
	for i in range(searchLen):
		subStr = haystack[i:i + needleLen]
		if subStr == search:
			count += 1
			break

print(count)