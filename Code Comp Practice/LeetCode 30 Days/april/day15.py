class Solution:
    def productExceptSelf(self, nums):
        arr = []
        p = 1
        for num in nums:
            arr.append(p)
            p *= num
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            arr[i] *= p
            p *= nums[i]
        return arr

sol = Solution()
res = sol.productExceptSelf([1,2,3,4])
print(res)