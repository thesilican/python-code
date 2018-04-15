import time

class Cell:
    def __init__(self):
        self.solvedNum = -1
        self.__allowedNums = [True for x in range (9)]
    def getAllowedNum(self, i):
        return self.__allowedNums[i-1]
    def setAllowedNum(self,i, b):
        self.__allowedNums[i - 1] = b

def printBoard(cells):
    print()
    print()
    for i in range(9):
        for j in range(9):
            print (" " if cells[i][j].solvedNum == -1 else cells[i][j].solvedNum, end = '')
        print()
    time.sleep(1)

def isCellsSolved(cells):
    for arr in cells:
        for c in arr:
            if c.solvedNum == -1:
                return False
    return True

def Solve(cells):
    while not isCellsSolved(cells) or not isImpossible:
        cells = SolveIter(cells)
        printBoard(cells)

def SolveIter(cells):
    newCells = cells
    for i in range(9):
        for j in range(9):
            newCells = FillIn(cells, i, j)
    return newCells

# Fill in the cell at the specified spot
def FillIn(cells, x, y):
    if cells[x][y].solvedNum != -1:
        return cells

    # Check each Row & Column
    for i in range(9):
        if cells[x][i].solvedNum != -1:
            cells[x][y].setAllowedNum(cells[x][i].solvedNum, False)
    for i in range(9):
        if cells[i][y].solvedNum != -1:
            cells[x][y].setAllowedNum(cells[i][x].solvedNum, False)
    #Check each 3x3 cell
    for i in range(x-(x%3), 3+x-(x%3)):
        for j in range(y-(y%3), 3+y-(y%3)):
            if cells[i][j].solvedNum != -1:
                cells[x][y].setAllowedNum(cells[i][j].solvedNum, False)

    allowed = 0
    allowedNum = -1
    for i in range(1,10):
        if cells[x][y].getAllowedNum(i) == True:
            allowed += 1
            allowedNum = i
    if allowed == 0:
        isImpossible = True
        return cells
    elif allowed == 1:
        cells[x][y].solvedNum = i
    return cells

isImpossible = False
puzzle = [[Cell() for i in range(9)] for i in range(9)]
file = open("Sudoku.txt")
for i in range(9):
    inputStr = file.readline()
    for j in range(9):
        c = Cell()
        if inputStr[j].isdigit():
            c.solvedNum = int(inputStr[j])
        puzzle[i][j] = c

printBoard(puzzle)
Solve(puzzle)
printBoard(puzzle)
print("Done!")