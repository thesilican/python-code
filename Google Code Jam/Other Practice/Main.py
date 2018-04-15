"""
Method format:
def SolveCase(inputStr):
    pass
should return a string

An automatic "Case #n:" will be added
"""
# Stuff for importing modules/files
import os
import importlib
os.system("clear")
print("Files must be in the same dir as Main.py")

modules = []
for obj in os.listdir():
    if obj.endswith(".py") and obj != "Main.py":
        modules.append(obj)
        print("[{}] - {}".format(len(modules) - 1, modules[-1]))

selected = int(input("> "))
if selected < 0 or selected >= len(modules):
    print("Error - must be greater or equal to 0 and less than {}".format(len(modules)))
    exit()
# Now import
SolveCase = importlib.import_module(modules[selected].replace(".py", "")).SolveCase
# Change the name of the module to change to different solvers:
FILENAME = "A-large-practice.in"

f = open(FILENAME)
cases = int(f.readline())
for i in range(cases):
    print("Case #" + str(i + 1) + ": " + SolveCase(f.readline()))
