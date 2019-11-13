onesDict = {
  0: "zero",
  1: "one",
  2: "two",
  3: "three",
  4: "four", 
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten"
}

teensDict = {
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
}

tensDict = {
  2: "twenty",
  3: "thirty",
  4: "forty",
  5: "fifty",
  6: "sixty",
  7: "seventy",
  8: "eighty",
  9: "ninety"
}

def stringify(num):
  if num <= 10:
    return onesDict[num]
  elif num <= 19:
    return teensDict[num]
  elif num <= 99:
    tens = tensDict[num // 10]
    ones = ((" " + onesDict[num % 10]) if num % 10 != 0 else "")
    return tens + ones
  elif num <= 999:
    hundreds = onesDict[num // 100]
    and_ = "" if num % 100 == 0 else "and "
    tensOnes = "" if num % 100 == 0 else stringify(num % 100)
    return hundreds + " hundred " + and_ + tensOnes
  elif num == 1000:
    return "one thousand"

def countChar(s):
  sum_ = 0
  for char in s:
    if char.isalpha():
      sum_ += 1
  return sum_

sum_ = 0
for i in [x + 1 for x in range(1000)]:
  stringified = stringify(i)
  sum_ += countChar(stringified)
print(sum_)