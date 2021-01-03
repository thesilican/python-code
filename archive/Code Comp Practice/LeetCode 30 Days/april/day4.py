class Solution:
    def moveZeroes(self, nums):
        l = len(nums)
        numZero = 0
        ptr = 0
        for i, num in enumerate(nums):
            while ptr < l and nums[ptr] == 0:
                ptr += 1
                numZero += 1
            if ptr == l:
                break
            nums[i] = nums[ptr]
            ptr += 1
        
        ptr += 1
        for i in range(l - numZero, l):
            nums[i] = 0


if __name__ == "__main__":
    arr = [1, 0]
    Solution().moveZeroes(arr)
    print(arr)
