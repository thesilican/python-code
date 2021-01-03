FILENAME = "Program.bf"

contents = "".join(open(FILENAME, "r").readlines())
commandList = []
for char in contents:
    if char in ["<", ">", "+", "-", ".", ",", "[", "]"]:
        commandList.append(char)
codepointer = 0
tape = [0 for i in range(3000)]
tapepointer = 0
inputbuffer = []

while codepointer < len(commandList):
    if commandList[codepointer] == "<":
        tapepointer -= 1
    elif commandList[codepointer] == ">":
        tapepointer += 1
    elif commandList[codepointer] == "+":
        tape[tapepointer] += 1
    elif commandList[codepointer] == "-":
        tape[tapepointer] -= 1
    elif commandList[codepointer] == ".":
        print(chr(tape[tapepointer]), end="")
    elif commandList[codepointer] == ",":
        while len(inputbuffer) == 0:
            inputbuffer.append([ord(x) for x in list(input())])
        tape[tapepointer] = inputbuffer.pop(0)
    elif commandList[codepointer] == "[":
        if tape[tapepointer] == 0:
            depth = 0
            codepointer += 1
            while codepointer < len(commandList) and (commandList[codepointer] != "]" or depth > 0):
                if (commandList[codepointer] == "["):
                    depth += 1
                elif (commandList[codepointer] == "]"):
                    depth -= 1
                codepointer += 1
    elif commandList[codepointer] == "]":
        if tape[tapepointer] != 0:
            depth = 0
            codepointer -= 1
            while codepointer >= 0 and (commandList[codepointer] != "[" or depth > 0):
                if (commandList[codepointer] == "["):
                    depth -= 1
                elif (commandList[codepointer] == "]"):
                    depth += 1
                codepointer -= 1
    codepointer += 1