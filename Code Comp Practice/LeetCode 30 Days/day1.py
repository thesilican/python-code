class Solution:
    def singleNumber(self, nums) -> int:
        d = {}
        for n in nums:
            if (n in d):
                del d[n]
            else:
                d[n] = True
        return list(d.keys())[0]

print(Solution().singleNumber([1,1,17,2,3,4,2,3,4]))