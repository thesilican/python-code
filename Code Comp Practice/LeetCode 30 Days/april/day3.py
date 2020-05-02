class Solution:
    def maxSubArray(self, nums):
        # Condense
        positive = nums[0] >= 0
        condensed = []
        acc = 0
        for i in nums:
            if positive != (i >= 0):
                positive = not positive
                condensed.append(acc)
                acc = 0
            acc += i
        condensed.append(acc)
        mx = None
        tri = [0 for x in condensed]
        for i, num in enumerate(condensed):
            for j in range(i + 1):
                tri[j] += num
                if (mx == None or tri[j] > mx):
                    mx = tri[j]
        return mx


if __name__ == "__main__":
    res = Solution().maxSubArray([7, 1, 1, -1, -1, 1, 1, 1, -1])
    print(res)
