# Brute force always works
largestP = 0
for i in range(1000):
    for j in range(1000):
        if i * j > largestP:
            s = str(i * j)
            flag = True
            for k in range(len(s) // 2 + 1):
                if s[k] != s[-(k+1)]:
                    flag = False
                    break
            if flag:
                largestP = int(s)
print (largestP)