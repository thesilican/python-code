hFlip = False
vFlip = False
for s in input():
    if (s == 'H'):
        hFlip = not hFlip
    if (s == 'V'):
        vFlip = not vFlip

if vFlip:
    if hFlip:
        print("4 3\n2 1")
    else:
        print("2 1\n4 3")
else:
    if hFlip:
        print("3 4\n1 2")
    else:
        print("1 2\n3 4")