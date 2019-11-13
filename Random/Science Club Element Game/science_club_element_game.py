one_letter = []
two_letter = []

with open("elements.csv", "r") as f:
  lines = [x.split(",")[1].strip() for x in f.readlines()]
  for l in lines:
    if len(l) == 1:
      one_letter.append(l)
    else:
      two_letter.append(l)

def validateWord(word):
  print(word)
  if len(word) == 0:
    return True
  for el in one_letter:
    if word.lower().startswith(el.lower()):
      if validateWord(word[1:]):
        return True
  if len(word) == 1:
    return False
  for el in two_letter:
    if word.lower().startswith(el.lower()):
      if validateWord(word[2:]):
        return True
  return False

if __name__ == "__main__":
  while True:
    print("Enter a word: ", end="")
    print(validateWord(input()))