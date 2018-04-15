def GetAttackDamage(instructions: list) -> int:
    total = 0
    d = 1
    for i in instructions:
        if i == "C":
            d *= 2
        else:
            total += d
    return total


def SolveCase(case):
    d, instructions = input().split(" ")
    instructions = list(instructions)
    d = int(d)
    # Impossible if #s > d
    if instructions.count("S") > d:
        print("Case #{}: IMPOSSIBLE".format(case))
        return

    # Otherwise just repeatedly move the right-most C up
    moves = 0
    while True:
        if (GetAttackDamage(instructions) <= d):
            print("Case #{}: {}".format(case, moves))
            return
        # Find the right-most C & swap with righter s
        foundS = False
        for i in range(len(instructions) - 1, -1, -1):
            if instructions[i] == "S":
                foundS = True
            elif foundS == True:
                temp = instructions[i]
                instructions[i] = instructions[i+1]
                instructions[i+1] = temp
                break
        moves += 1


numCases = int(input())
for i in range(numCases):
    SolveCase(i + 1)
