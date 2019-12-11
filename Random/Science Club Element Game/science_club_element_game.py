#!/usr/bin/env python3
from validation import validateWord, isScrabbleWord

# Enter filenames
fileTexts = []

while True:
    print("Enter a txt filename of words: ", end="")
    filename = input()
    if filename == "":
        break
    try:
        # Open and read file
        with open(filename + ".txt", "r") as f:
            lines = f.readlines()
            # De-duplicate
            words = list(set([x.lower().strip() for x in lines]))
        print("    " + filename + ".txt successfully loaded")
        print("    " + str(len(words)) + " words found")

        # Validate words
        validWords = list(filter(validateWord, filter(isScrabbleWord, words)))
        print("    " + str(len(validWords)) + " valid words found")
        print("    Invalid words: ")
        invalidWords = list(set(words) - set(validWords))
        for w in invalidWords:
            print("        " + w)
        fileTexts.append([filename, tuple(validWords) , len(validWords), len(invalidWords)])
    except FileNotFoundError:
        print("File " + filename + ".txt not found")
        continue

# Remove duplicates
for i, submission in enumerate(fileTexts):
    this = set(submission[1])
    others = set()
    for j, other in enumerate(fileTexts):
        if i == j:
            continue
        others.update(other[1])
    diff = this - others
    submission.append(len(diff))
    submission.append(diff)
    print(submission[0], "has", len(diff), "unique terms")

def sortByUnique(val):
    return val[4]

fileTexts.sort(key=sortByUnique, reverse=True)

print("\n\n\n---------- Results ----------")
for i, submission in enumerate(fileTexts):
    print(str(i + 1) + ")", submission[0],"-",submission[4],"unique words:")
    print("    " + ", ".join(sorted(submission[5])))
    print("-"*29)