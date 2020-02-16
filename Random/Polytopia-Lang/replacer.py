#!/usr/bin/python3
import json
obj = json.loads(open("en_US.json", "r").read())

for key, val in obj.items():
    val = val.replace("o", "owo") \
        .replace("u", "uwu")\
        .replace("O", "OwO")\
        .replace("U", "UwU")
    val += " nya"
    obj[key] = val

obj["language"] = "Languwuage"

open("lang.json", "w").write(json.dumps(obj))
