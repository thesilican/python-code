from itertools import permutations
nums = permutations(range(-169//3,169//3 + 2), 3)

incr = 1
for i in nums:
    if (i[0] ** 2) + (i[1] ** 2) + (i[2] ** 2) == 169:
        print (f"{incr}: {i[0]}^2 + {i[1]}^2 {i[2]}^2 = 169")
        incr += 1
