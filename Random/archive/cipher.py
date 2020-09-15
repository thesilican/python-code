WORDS = {}
with open("words_alpha.txt", "r") as f:
    allwords = map(str.strip, f.readlines())
    for word in allwords:
        if len(word) not in WORDS:
            WORDS[len(word)] = []
        WORDS[len(word)].append(word)
ALPHABET = [chr(x) for x in range(97, 123)]

def findMatching(word, d):
    l = len(word)
    pool = WORDS[l]
    matchChars = []
    for c in word:
        matchChars.append(d[c])
    match = []
    for poolWord in pool:
        valid = True
        for i in range(l):
            if poolWord[i] not in matchChars[i]:
                valid = False
        if valid:
           match.append(poolWord)
    return match 

def eliminate(words, d):
    for word in words:
        matching = findMatching(word, d)
        # Todo
        

def solve(text):
    d = dict((x, set(ALPHABET)) for x in ALPHABET)
    words = text.lower().split()
    # Todo


text = input().split()
print(solve(text))