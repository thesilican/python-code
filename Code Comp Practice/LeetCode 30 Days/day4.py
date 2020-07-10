class Solution:
    def findComplement(self, num: int) -> int:
        cpy = num
        mask = 0
        while cpy != 0:
            cpy >>= 1
            mask = (mask << 1) + 1
        return ~num & mask
        