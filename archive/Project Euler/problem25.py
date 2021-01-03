import time

def fib():
	yield 1
	yield 1
	num1 = 1
	num2 = 1
	while True:
		num1, num2 = num2, num1 + num2
		yield num2

index = 0
for f in fib():
	index += 1
	if len(str(f)) == 1000:
		print (index)
		break