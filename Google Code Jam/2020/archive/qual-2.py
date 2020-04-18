def case(caseNum):
    curNum = 0
    s = ""
    nums = [int(x) for x in input()]
    for i in nums:
        if i > curNum:
            s += "(" * (i - curNum)
        elif i < curNum:
            s += ")" * (curNum - i)
        s += str(i)
        curNum = i
    if curNum > 0:
        s += ")" * curNum
        
    print("Case #{}: {}".format(caseNum, s))


t = int(input())
for i in range(t):
    case(i + 1)