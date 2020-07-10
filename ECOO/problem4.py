def case():
    N = int(input())
    code = ["x=0;C=1000000007"]
    x = 0
    stack = []

    def transpile(line):
        if line[0] == "FUN":
            stack.append([line[1]])
        elif line[0] == "END":
            funcDef = stack.pop()
            name = funcDef.pop(0)
            args = map(transpile, funcDef)
            return "def " + name + "():\n global x\n " + "\n ".join(args)
        elif len(stack) > 0:
            stack[-1].append([line[0], line[1]])
        elif line[0] == "ADD":
            return "x=(x+" + line[1] + ")%C"
        elif line[0] == "SUB":
            return "x=(x-" + line[1] + ")%C"
        elif line[0] == "MULT":
            return "x=(x*" + line[1] + ")%C"
        elif line[0] == "CALL":
            return line[1] + "()"
    for _ in range(N):
        res = transpile(input().split())
        if res != None:
            code.append(res)
    d = {}
    # Please, never do this
    exec("\n".join(code), d)
    print(d['x'])


T = int(input())
for i in range(T):
    case()