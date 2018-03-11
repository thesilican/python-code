# Variables, Constants and Literals

# I am a variable. Yay
aVariable = 25
print(str(aVariable) + "\n")

# Some cool multi-variable declarations
a, b, c = 5, 3.2, "Hello"

print(a)
print(b)
print(c)

x = y = z = "same"

print(x)
print(y)
print(z)
print()

# Constant variables
import program4_constants
print(program4_constants.Variable)
# program4_constants.StringVariable = "HII"
print(program4_constants.StringVariable)

# Naming Conventions:
#   Regular variable = camelCase
#   Constant = ALL_CAPS

# ---------- Literals ----------
a = 0b1010  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # Octal Literal
d = 0x12c  # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string
with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

drink = "Available"
food = None


def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)


menu(drink)
menu(food)

fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)
