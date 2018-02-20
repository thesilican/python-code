"""
Method format:
def SolveCase(inputStr):
    pass
should return a string

An automatic "Case #n:" will be added
"""
# Change the name of the module to change to different solvers:
from GCJ_2015_Qual_A import SolveCase
FILENAME = "A-large-practice.in"

f = open(FILENAME)
cases = int(f.readline())
for i in range(cases):
    print("Case #" + str(i + 1) + ": " + SolveCase(f.readline()))
