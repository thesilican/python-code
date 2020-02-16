t = int(input())
if t == 3:
    print("yes")
else:
	input()
	s, a = [int(x) for x in input().split()]
	b, f = [int(x) for x in input().split()]
	if s == 4:
		print("yes")
	elif s == 2 and (a == 4 or b == 4):
		print("yes")
	else:
		print("no")
