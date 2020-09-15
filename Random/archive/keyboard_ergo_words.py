#!/usr/bin/python3

# qwerty keyboard:
keys = [
    ["q","a","z"],
    ["w","s","x"],
    ["e","d","c"],
    ["r","f","v", "t","g","b"],
    ["y","h","n","u","j","m"],
    ["i","k"],
    ["o","l"],
    ["p"]
]

KEYMAP = {}
for i, group in enumerate(keys):
    for key in group:
        KEYMAP[key] = i

with open("words_alpha.txt") as f:
    content = [x.strip() for x in f.readlines()]
    for word in content:
        hash = []
        for c in word:
            hash.append(KEYMAP[c])
        if len(hash) >= 8 and hash[0] > 3 == hash[2] > 3 and hash[2] > 3 == hash[4] > 3 and hash[4] > 3 == hash[6] > 3:
            if hash[1] > 3 == hash[3] > 3 and hash[3] > 3 == hash[5] > 3 and hash[5] > 3 == hash[7] > 3:
                if hash[0] > 3 != hash[1] > 3:
                    print("GOOD", word)
                    if sorted(hash) == [0,1,2,3,4,5,6,7]:
                        print(word)

