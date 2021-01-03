collatzDict = {1: 1}


def lenCollatz(n):
  if n <= 0:
    return -1
  chain = []
  curNum = n
  chain.append(curNum)

  while not curNum in collatzDict:
    if curNum % 2 == 0:
      curNum = curNum // 2
    else:
      curNum = curNum * 3 + 1
    chain.append(curNum)

  chainLen = len(chain)
  curNumLen = collatzDict[curNum]
  for i in range(len(chain)):
    length = curNumLen + chainLen - i - 1
    collatzDict[chain[i]] = length
  
  return chainLen + curNumLen - 1

if __name__ == "__main__":
  mx = 0
  for x in range(1_000_000):
    length = lenCollatz(x)
    if length > mx:
      mx = length
      print(x, "has a chain length of", length)
