def SolveCase(case):
    distance, horses = [int(x) for x in input().split(" ")]
    max_hours = 0
    for i in range(horses):
        hdist, hspeed = [int(x) for x in input().split(" ")]
        max_hours = max((distance - hdist) * (1/hspeed), max_hours)
    print("Case #{}: {}".format(case, distance/max_hours))


numCases = int(input())
for i in range(numCases):
    SolveCase(i + 1)
