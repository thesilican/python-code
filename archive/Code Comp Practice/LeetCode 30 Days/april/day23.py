import random

class Solution:
    def rangeBitwiseAnd(self, m, n):
        p = 1
        bitmask = (2 ** 31) - 1
        res = 0
        while p <= n:
            if n & p and m >= n & bitmask:
                res += p
            bitmask -= p
            p *= 2
        return res


def bruteForce(m, n):
    res = n
    for i in range(m, n):
        res &= i
    return res

for i in range(10000):
    pool = [random.randint(0, 1000) for x in (1, 2)]
    m = min(pool)
    n = max(pool)
    res = Solution().rangeBitwiseAnd(m, n)
    assert res == bruteForce(m, n)
