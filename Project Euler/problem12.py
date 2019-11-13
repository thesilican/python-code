from util_numbers import triangleNums, getFactors

for num in triangleNums(0):
  numFactors = getFactors(num)
  print (num, len(numFactors))
  if len(numFactors) >= 500:
    print(num)
    break