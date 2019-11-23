from util_numbers import triangleNums, getDivisors

for num in triangleNums(0):
  numFactors = getDivisors(num)
  print (num, len(numFactors))
  if len(numFactors) >= 500:
    print(num)
    break