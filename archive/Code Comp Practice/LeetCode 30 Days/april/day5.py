import itertools
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        down = prices[1] < prices[0]
        l = prices[0]
        s = 0
        for i, num in enumerate(itertools.islice(prices, 2, None)):
            if num < prices[i + 1]:
                if not down:
                    down = True
                    s += prices[i + 1] - l
            else:
                if down:
                    down = False
                    l = prices[i + 1]
        if not down:
            s += prices[-1] - l
        return s

if __name__ == "__main__":
    sol = Solution().maxProfit([1,2,3,4,3,4,6,5,5])
    print(sol)