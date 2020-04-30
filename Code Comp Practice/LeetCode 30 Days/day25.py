import timeit
import random


class Solution:
    def canJump(self, nums):
        furthest = 0
        for i in range(len(nums)):
            if i > furthest:
                return False
            if i + nums[i] > furthest:
                furthest = i + nums[i]
        return True


sol = Solution()
print()
print(sol.canJump([2, 3, 1, 0, 1, 4]))

# res = min(timeit.repeat(
#     "sol.canJump(arr)", "arr = [random.randint(0, 10) for _ in range(10_000)]", globals=globals(), number=1, repeat=1))
# print(res)
