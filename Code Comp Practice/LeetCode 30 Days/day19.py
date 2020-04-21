class Solution:
    def binSearch(self, low, high, nums, target, split):
        pivot = (high + low) // 2
        pVal = nums[pivot]
        firstHalf = False
        if target < pVal:
            if split < target:
                firstHalf = True
            elif split < pVal:
                firstHalf = False
            else:
                firstHalf = True
        elif target > pVal:
            if split < pVal:
                firstHalf = False
            elif split < target:
                firstHalf = True
            else:
                firstHalf = False
        else:
            return pivot
        if high - low == 1:
            return -1
        if firstHalf:
            return self.binSearch(low, pivot, nums, target, split)
        else:
            return self.binSearch(pivot, high, nums, target, split)

    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        split = nums[0]
        if target == split:
            return 0
        return self.binSearch(0, len(nums), nums, target, split)

l = 1_000_000
p = l // 6

sol = Solution()
nums = list(range(p, l)) + list(range(0, p))
nums = [4,5,6,7,0,1,2]
res = sol.search(nums, -1)
print(res)
