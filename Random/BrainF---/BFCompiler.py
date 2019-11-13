import os

FILENAME = "Program.bf"
CSFILENAME = "Program.cs"
COMPILER = "C:/Windows/Microsoft.NET/Framework/v3.5/csc.exe"
OUTFILENAME = "Program.exe"
ARRAYLIMIT = 1000
contents = "".join(open(FILENAME, "r").readlines())
commandList = []
for char in contents:
    if char in ["<", ">", "+", "-", ".", ",", "[", "]"]:
        commandList.append(char)

lines = []
lines.append("using System;")
lines.append("class Program {")
lines.append("public static void Main(string[] args) {")
lines.append("int[] arr = new int[" + str(ARRAYLIMIT) + "];")
lines.append("int ptr = 0;")
lines.append("Action l = () => {ptr = (ptr + 1 + " + str(ARRAYLIMIT) + ") %" + str(ARRAYLIMIT)+ ";};")
lines.append("Action r = () => {ptr = (ptr -1 + " + str(ARRAYLIMIT) + ") %" + str(ARRAYLIMIT)+ ";};")
lines.append("Action i = () => {arr[ptr]++;};")
lines.append("Action d = () => {arr[ptr]--;};")
lines.append("Action p = () => {Console.Write((char)arr[ptr]);};")
lines.append("Action g = () => {arr[ptr] = Console.Read();};")
for char in commandList:
    if char == "<":
        lines.append("l();");
    elif char == ">":
        lines.append("r();")
    elif char == "+":
        lines.append("i();")
    elif char == "-":
        lines.append("d();")
    elif char == ".":
        lines.append("p();")
    elif char == ",":
        lines.append("g();")
    elif char == "[":
        lines.append("while(arr[ptr] != 0) {")
    elif char == "]":
        lines.append("}")
lines.append("}")
lines.append("}")

with open(CSFILENAME, "w") as outfile:
    outfile.write("\n".join(lines))

os.system(COMPILER + " /out:\"" + OUTFILENAME + "\" \"" + CSFILENAME + "\"")