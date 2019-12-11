one_letter = []
two_letter = []
scrabble_words = []

with open("data_elements", "r") as f:
    lines = [x.split(",")[1].strip() for x in f.readlines()]
    for l in lines:
        if len(l) == 1:
            one_letter.append(l)
        else:
            two_letter.append(l)

with open("data_dictionary", "r") as f:
    scrabble_words = [x.strip().lower() for x in f.readlines()]

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