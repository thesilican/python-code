# Type Conversion
# So, basically there's implicit type casting...
jeSuisInt = 100  # An int!
jeSuisFloat = 200.0  # A float!

print("First number is {}".format(type(jeSuisInt)))
print("Second number is {}".format(type(jeSuisFloat)))
# Always casted to a larger data type
print("Sum is {}".format(type(jeSuisInt+jeSuisFloat)))
print()

# ...and explicit type casting
# using [type](expression)
# ie. int("10") or list("abcdefg")
num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))
