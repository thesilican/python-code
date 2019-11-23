def genNumbers(inpt):
    nums = list(inpt)
    extra = ["0"]
    for i in range(len(nums)):
        if nums[i] == "4":
            nums[i] = "3"
            extra.append("1")
        else:
            extra.append("0")
    return "".join(nums), "".join(extra).lstrip("0")


t = int(input())
for i in range(t):
    inpt = input()
    nums, extra = genNumbers(inpt)
    print ("Case #" + str(i + 1) + ": " + nums + " " + extra)