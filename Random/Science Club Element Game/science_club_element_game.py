one_letter = []
two_letter = []
scrabble_words = []

with open("elements.csv", "r") as f:
    lines = [x.split(",")[1].strip() for x in f.readlines()]
    for l in lines:
        if len(l) == 1:
            one_letter.append(l)
        else:
            two_letter.append(l)

with open("dictionary.txt", "r") as f:
    scrabble_words = [x.strip().lower() for x in f.readlines()]

def validateWord(word):
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


def isScrabbleWord(word):
    def binarySearch(min_, max_):
        mid = (max_-min_)//2 + min_
        if scrabble_words[mid] == word.lower():
            return True
        elif min_ >= max_:
            return False
        else:
            if word.lower() > scrabble_words[mid]:
                return binarySearch(mid + 1, max_)
            else:
                return binarySearch(min_, mid - 1)
    return binarySearch(0, len(scrabble_words) - 1)


if __name__ == "__main__":
    while True:
        print("Enter a filename of words: ", end="")
        filename = input()
        validwords = []
        invalidwords = []
        with open(filename, "r") as f:
            lines = [x.lower().strip() for x in f.readlines()]
            for word in lines:
                isValid = validateWord(word)
                isScrabble = isScrabbleWord(word)
                if isValid and isScrabble:
                    validwords.append(word)
                else:
                    invalidwords.append(word)
        print("Number of valid words found:", len(validwords))
        print("---------- Valid words: ----------")
        for word in validwords:
            print(word)
        print("---------- Invalid words: ----------")

