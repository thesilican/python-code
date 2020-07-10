ALPHABET = [chr(x) for x in range(97,123)]
ROT13 = dict([(ALPHABET[x], ALPHABET[(x+13)%26]) for x in range(26)])

# words = []
# with open("words_alpha.txt", "r") as f:
#     words.extend((x.strip() for x in f.readlines()))
# rotwords = []

# for i, word in enumerate(words):
#     newword = ""
#     for c in word:
#         newword += ROT13[c]
#     rotwords.append(newword)
#     print(i, "/", len(words))
    

# with open("words_rot13.txt", "w") as f:
#     f.write("\n".join(rotwords))

# words = set()
# with open("words_alpha.txt", "r") as f:
#     words.update((x.strip() for x in f.readlines()))
# rotwords = []
# with open("words_rot13.txt", "r") as f:
#     rotwords.extend((x.strip() for x in f.readlines()))
# validwords = []

# for i, word in enumerate(rotwords):
#     if word in words:
#         validwords.append(word)
#     print(i, "/", len(rotwords))

# with open("words_rot13_valid.txt", "w") as f:
#     f.write("\n".join(validwords))

words = []
with open("words_rot13_valid.txt", "r") as f:
    words.extend((x.strip() for x in f.readlines()))

rotwords = []
for i, word in enumerate(words):
    newword = ""
    for c in word:
        newword += ROT13[c]
    rotwords.append(newword)
print("\n".join((x[1] + " - " + x[0] for x in zip(words, rotwords))))