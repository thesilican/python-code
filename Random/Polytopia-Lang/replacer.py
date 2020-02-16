#!/usr/bin/python3
import json
import random
obj = json.loads(open("en_US.json", "r").read())

for key, val in obj.items():
    # val = val.replace("o", "owo") \
    #     .replace("u", "uwu")\
    #     .replace("O", "OwO")\
    #     .replace("U", "UwU")
    # val += " nya"
    # obj[key] = val
    words = ["UwU", "OwO", "Nya"]
    obj[key] = random.choice(words)

obj["language"] = "Languwuage"

open("lang1.json", "w").write(json.dumps(obj))
