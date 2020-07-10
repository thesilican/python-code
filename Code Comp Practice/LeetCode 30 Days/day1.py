badVersion = [0] + [False for _ in range(1)] + [True for _ in range(1)]


def isBadVersion(n):
    return badVersion[n]


class Solution:
    def firstBadVersion(self, n):
        if isBadVersion(1):
            return 1
        minRange = 1
        maxRange = n
        while maxRange - minRange > 1:
            mid = (maxRange + minRange) // 2
            if isBadVersion(mid):
                maxRange = mid
            else:
                minRange = mid
        return maxRange


print(Solution().firstBadVersion(len(badVersion) - 1))
