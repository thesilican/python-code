class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = set()
        for c in J:
            d.add(c)
        t = 0
        for c in S:
            if c in d:
                t += 1
        return t
