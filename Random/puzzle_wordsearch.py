words = []
with open("words_alpha.txt", "r") as f:
    words = [x.strip() for x in f.readlines()]

wordsearch = []
with open("wordsearch.txt", "r") as f:
    for line in f.readlines():
        arr = []
        for c in line.strip():
            arr.append(c)
        wordsearch.append(arr)

coordDict = dict((chr(x),[]) for x in range(97,123))
for i in range(len(wordsearch)):
    for j in range(len(wordsearch[0])):
        if wordsearch[i][j] not in coordDict:
            coordDict[wordsearch[i][j]] = []
        coordDict[wordsearch[i][j]].append((i, j))

DIRS = [
    (1, 1),
    (1, 0),
    (1, -1),
    (0, 1),
    (0, -1),
    (-1, 1),
    (-1, 0),
    (-1, -1)
]


def search(word):
    l = len(word)
    lenX = len(wordsearch)
    lenY = len(wordsearch[0])
    for x, y in coordDict[word[0]]:
        for dX, dY in DIRS:
            i, j = x, y
            p = 0
            while p < l and 0 <= i < lenX and 0 <= j < lenY:
                if word[p] != wordsearch[i][j]:
                    break
                p += 1
                i += dX
                j += dY
            if p == l:
                return True
    return False


WORDSEARCH_WORDS = [
    "bach",
    "mozart",
    "beethoven",
    "tchaikovsky",
    "wagner",
    "brahms",
    "schubert",
    "rossini",
    "handel",
    "haydn",
    "vivaldi",
    "stravinsky",
    "mendelssohn",
    "rachmaninov",
    "chopin",
    "debussy",
    "liszt",
    "dvorak"
]
validwords = []
# for word in set(words + WORDSEARCH_WORDS):
for word in WORDSEARCH_WORDS:
    if len(word) < 5:
        continue
    if search(word):
        validwords.append(word)
        print(word)
