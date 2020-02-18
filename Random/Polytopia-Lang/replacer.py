#!/usr/bin/python3
import json
import random
import re
obj = json.loads(open("en_US.json", "r").read())

acc = 0
for key, val in obj.items():
    matches = re.findall("\\{\\d\\}", val)
    matchStr = " ".join(matches)
    words = ["UwU", "OwO", "Nya"]
    obj[key] = (matchStr + " " + words[acc % 3]).strip()
    acc += 1
    print(obj[key])

obj["language"] = "Languwuage"

open("lang1.json", "w").write(json.dumps(obj))
