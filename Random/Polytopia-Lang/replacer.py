#!/usr/bin/python3
import json
import random
import re
obj = json.loads(open("en_US.json", "r").read())

for key, val in obj.items():
    matches = re.findall("\\{\\d\\}", val)
    matchStr = " ".join(matches)
    words = ["UwU", "OwO", "Nya"]
    obj[key] = (matchStr + " " + random.choice(words)).strip()
    print(obj[key])

obj["language"] = "Languwuage"

open("lang1.json", "w").write(json.dumps(obj))
