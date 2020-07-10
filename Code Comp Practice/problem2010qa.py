t = int(input())
for case in range(1, t + 1):
	splits = input().split()
	n = int(splits[0])
	k = int(splits[1])
	bit = k & (2**(n-1))
	print("Case #" + str(case) + ":", "OFF" if bit == 0 else "ON")