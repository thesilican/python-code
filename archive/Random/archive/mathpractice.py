import sys
import datetime
MIN = 1
MAX = 12
start = datetime.datetime.now()

for i in range(MIN, MAX + 1):
	for j in range(MIN, MAX + 1):
		ans = -1
		while ans != i * j:
			print(str(i) + "x" + str(j) + "? ", end="")
			try:
				ans = int(input())
			except ValueError:
				ans = -1
end = datetime.datetime.now()
elapsed = end - start
print("Answered " + str(MAX - MIN + 1) + " questions in " + elapsed.total_seconds())