# Data types

# First of all, we have the 3 types of numbers
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))

# Here are lists:
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# or this does the same thing
l = list(range(10))
print("l = ", l)
print("l[2] = ", l[2])
# slicing
print("l[2:] = ", l[2:])
print("l[5:6] = ", l[5:6])

# Tuples
t = (1, 2, 3, 4, 5)
print(t)
# Basically the same as lists, but they are immutable
try:
    t[0] = 100
except Exception as e:
    print(e)

# Strings
string = "A single-line string"
multi_string = """A multi line
string sequence
wow!"""
print(string)
print(multi_string)
# They're also iterable...
print(string[5])
print(multi_string[2:12])
# ...but also immutable
try:
    string[0] = 'd'
except Exception as e:
    print(e)

# Set
a = {5, 2, 3, 1, 4, 1, 2, 2, 3, 4, 5, 5, 5}
# printing set variable
print("a = ", a)
# data type of variable a
print(type(a))

# Dictionary
d = {"a": "Apple",
     "b": "Banana",
     "c": "Carrot"}
print("d[1] = ", d["a"])
print("d['key'] = ", d["b"])
# Generates error
try:
    print("d[2] = ", d[2])
except Exception as e:
    print(e)

# Type conversion
# As easy as type()
print(float(5))
print(int(10.6))
print(int(-10.6))
print(str(int("10")))
