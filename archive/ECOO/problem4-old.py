x = 0


def case():
    global x
    N = int(input())
    x = 0
    funcs = {}
    stack = []

    def execute(line, y=None):
        global x
        if line == "FUN":
            stack.append([y])
        elif line == "END":
            funcDef = stack.pop()
            name = funcDef.pop(0)
            funcs[name] = funcDef
        elif len(stack) > 0:
            stack[-1].append([line, y])
        elif line == "ADD":
            x = x + int(y) % 1000000007
        elif line == "SUB":
            x = x + int(y) % 1000000007
        elif line == "MULT":
            x = x * int(y) % 1000000007
        elif line == "CALL":
            for l in funcs[y]:
                execute(*l)
    for _ in range(N):
        line = input()
        execute(*(line.split()))
    print(x % 1000000007)


T = int(input())
for i in range(T):
    case()
