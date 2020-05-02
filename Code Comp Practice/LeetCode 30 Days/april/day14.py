from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sft = -sum((x[0] * 2 - 1) * x[1] for x in shift)
        sft = sft % len(s)
        return s[sft:] + s[:sft]



sol = Solution()
res = sol.stringShift("abc", [[0,1],[1,5]])
print(res)