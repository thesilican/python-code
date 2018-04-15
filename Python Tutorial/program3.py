# Statements, Indentation, Comments

# Multiline statements (Implicit)
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a)

# Multiline statements (Explicit)
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
print(a)

# Multiple statements on one line
a = 1; b = 2; c = 3
print(a, b, c)


# Docstring
def test():
    """I am a Docstring

    Returns:
        int -- the number 1
    """
    return 1

print(test.__doc__)
