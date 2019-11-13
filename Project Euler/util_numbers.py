from typing import List
from math import sqrt, ceil

def getFactors(number: int, sort: bool = True) -> List[int]:
  factors = set()
  for i in range(1, ceil(sqrt(number)) + 1):
    if number % i == 0:
      factors.add(i)
      factors.add(number // i)
  if sort:
    return sorted(factors)
  else:
    return list(factors);

if __name__ == "__main__":
    print(getFactors(12))
    print(getFactors(1000))
    print(getFactors(112123123412345))
    print(getFactors(112123123412345123456))


# Triangle Numbers
def triangleNums(num):
  """Generates the first n triangle numbers
  
  Arguments:
      num {int} -- the number of triangle numbers to return
  """
  accumulator = 0
  num = 1
  while num <= num:
    accumulator += num
    num += 1
    yield accumulator
  
def triangleNumsUpTo(upTo):
  """Generate all the triangle numbers up to a certain number
  
  Arguments:
      upTo {int} -- The triangle number to go up to. Set to 0 for an infinite generator!
  """
  accumulator = 0
  num = 1
  while num <= upTo or upTo == 0:
    accumulator += num
    num += 1
    yield accumulator

def sumDigits(num):
  """Returns the sum of all the digits in a number
    Thanks to https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python
  Arguments:
      bigNumber {int} -- The number to sum the digits of
  """
  acc = 0
  while num:
    acc, num = acc + num % 10, num // 10
  return acc
