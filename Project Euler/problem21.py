# Brute force once again
import primetools
from typing import Tuple


def isAmicable(n: int) -> Tuple[bool, int]:
    divSum = sum(primetools.getAllDivisors(n))
    if sum(primetools.getAllDivisors(divSum)):
        # divSum & n are amicable numbers
        return (True, divSum)
    return (False, 0)

print(isAmicable(220))

nums = set()
for i in range(1,100):
    if i in nums:
        continue
    res = isAmicable(i)
    if res[0]:
        # i & res[1] are amicable numbers
        nums.add(i)
        nums.add(res[1])
print(sum(nums))