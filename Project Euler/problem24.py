import itertools
perms = itertools.permutations(range(10))
i = 0
for perm in perms:
	i += 1
	if (i == 1_000_000):
		print (perm)
		break