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
    return word in scrabble_words