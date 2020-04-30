class Solution:
    def subarraySum(self, nums, k):
        d = {}
        runningSum = 0
        for i, num in enumerate(nums):
            runningSum += num
            if runningSum in d:
                d[runningSum].append(i)
            else:
                d[runningSum] = [i]

        res = 0
        for s in d:
            if s == k:
                res += len(d[s])
            if s - k in d:
                l = s - k
                lArr = d[l]
                rArr = d[s]
                lPtr = len(lArr) - 1
                rPtr = len(rArr) - 1
                while lPtr >= 0 and rPtr >= 0:
                    if rArr[rPtr] > lArr[lPtr]:
                        rPtr -= 1
                        res += lPtr + 1
                    else:
                        lPtr -= 1
        return res

sol = Solution()
arr = [1, 2, 0, -2, 2]
k = 2
res = sol.subarraySum(arr, k)
print(res)