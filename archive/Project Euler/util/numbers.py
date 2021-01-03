from typing import List
from math import sqrt, ceil

def getDivisors(number: int, sort: bool = True) -> List[int]:
  """Get all the divisors of a number

  Example: getDivisors(12) -> [1, 2, 3, 4, 6, 12]

  Arguments:
    number {int} -- The number to find divisors of
    sort {bool} -- Whether or not to sort the returned divisors
  """
  factors = set()
  for i in range(1, ceil(sqrt(number)) + 1):
    if number % i == 0:
      factors.add(i)
      factors.add(number // i)
  if sort:
    return sorted(factors)
  else:
    return list(factors)

def getProperDivisors(number: int, sort: bool = True) -> List[int]:
  """Get all the divisors less than number.
  Similar to getDivisors except only for numbers less than the number

  Example: getProperDivisors(12) -> [1, 2, 3, 4, 6]
  Arguments:
    number {int} -- The number to find divisors of
    sort {bool} -- Whether or not to sort the returned divisors
  """
  res = getDivisors(number, sort)
  res.remove(number)
  return res

if __name__ == "__main__":
    print(getDivisors(12))
    print(getDivisors(1000))
    print(getDivisors(112123123412345, True))
    print(getDivisors(112123123412345123456))


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
