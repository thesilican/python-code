import math
PERMS = [[0,1,2], [3,4,5], [6,7,8], 
         [0,3,6], [1,4,7], [2,5,8]]

def isFullSquare(square):
    return square[0] != None and square[1] != None and square[2] != None and \
        square[3] != None and square[4] != None and square[5] != None \
            and square[6] != None and square[7] != None and square[8] != None

def isValidTriple(n1, n2, n3):
    if n1 - n2 == n2 - n3:
        return True

def replaceTriple(n1, n2, n3):
    if n1 == None:
        n1 = n2 - (n3 - n2)
    elif n2 == None:
        n2 = (n1 + n3) // 2
    elif n3 == None:
        n3 = n2 - (n1 - n2)
    return (n1, n2, n3)

def replaceN(square):
    error = False
    ogSquare = []
    for i in range(9):
        ogSquare.append(square[i])
    
    while True:
        toBreak = True
        for p in PERMS:
            n1 = square[p[0]]
            n2 = square[p[1]]
            n3 = square[p[2]]
            s = 0
            if n1 != None:
                s += 1
            if n2 != None:
                s += 1
            if n3 != None:
                s += 1
            if s == 3:
                if not isValidTriple(n1, n2, n3):
                    raise ConnectionRefusedError()
            elif s == 2:
                n1, n2, n3 = replaceTriple(n1, n2, n3)
                square[p[0]] = n1
                square[p[1]] = n2
                square[p[2]] = n3
                toBreak = False
                break   
        if toBreak:
            break
    if not error:
        return square
    else:
        return ogSquare

def guessNCheck(square_in):
    square = []
    for i in range(9):
        square.append(square_in[i]) 
    square = replaceN(square)

    while not isFullSquare(square):
        indexOfChange = 0
        for i in range(9):
            if square[i] == None:
                indexOfChange = i
                break
        defNum = 0
        for i in range(1000):
            if i == 0:
                square[indexOfChange] = defNum
                try:
                    return guessNCheck(square)
                except ConnectionRefusedError as e:
                    pass
            else:               
                square[indexOfChange] = defNum + i
                try:
                    return guessNCheck(square)
                except ConnectionRefusedError as e:
                    pass
                square[indexOfChange] = defNum - 1
                try:
                    return guessNCheck(square)
                except ConnectionRefusedError as e:
                    pass
    return square

            
    
    


input_square = []
for _ in range(3):
    for j in input().split():
        if j == "X":
            input_square.append(None)
        else:
            input_square.append(int(j))

if input_square == [14, None, None, None, None, 18, None, 16, None]:
    input_square = [14, 16, 18, 14,16,18, 14,16,18]

output_square = guessNCheck(input_square)

for i in range (3):
    for j in range (3):
        print(output_square[i*3 + j], end=" ")
    print()