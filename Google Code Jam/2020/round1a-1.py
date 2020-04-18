def case(caseNum):
    N = int(input())
    strs = []
    strsF = []
    for x in range(N):
        strs.append(input())
    start = ""
    end = ""

    # For each string
    for i in range(N):
        s = strs[i]
        splits = s.split("*")
        sStart = splits[0]
        if sStart.startswith(start):
            start = sStart
        elif start.startswith(sStart):
            pass
        else:
            print("Case #{}: *".format(caseNum))
            return
        splits[0] = ""

        sEnd = splits[-1]
        if sEnd.endswith(end):
            end = sEnd
        elif end.endswith(sEnd):
            pass
        else:
            print("Case #{}: *".format(caseNum))
            return
        splits[-1] = ""

        strsF.append(splits)
    finalStr = start
    for s in strsF:
        finalStr += "".join(s)
    finalStr += end

    print("Case #{}: {}".format(caseNum, finalStr))


t = int(input())
for i in range(t):
    case(i + 1)
