# Input, Output and Import
# Output: print()
print('This sentence is output to the screen')
# Output: This sentence is output to the screen

a = 5

print('The value of a is', a)
# Output: The value of a is 5

# Actual syntax is print(*objects, sep=' ', end='\n',
#                          file=sys.stdout, flush=False)
print(1, 2, 3, 4, 5, sep="hello", end="!DONE\n")
print(1, 2, 3, 4, 5, sep=", ", end="!\n")
# Fancy formatting
print("Isn't {} just so {}?!".format("this", "cool"))
x = 1
y = 2
print("{1} + {0} = {2}".format(x, y, x+y))
# keywords work too!
print("Hello {name}, {greeting}".format(
    name="Bobby", greeting="ur a nice dude"))
# even cooler formatting
x = 1234.56789
print('The value of x is %3.2f' % x)


# Input: input()
print("Number + 1 = {}".format(int(input("Enter a number > "))+1))


# Importing
# A python module is a file containing python definitions & statements
# They end with a .py extension
import math

print(math.pi)
