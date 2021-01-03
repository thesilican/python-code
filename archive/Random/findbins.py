import re
from os import listdir
from os.path import isfile, join
from termcolor import colored

path = "/usr/bin"
filesAndDirs = listdir(path)
files = sorted(f for f in filesAndDirs if isfile(join(path, f)))

goodFiles = []
pattern = re.compile(r"^#! ?/")

for filename in files:
    filepath = join(path, filename)
    with open(filepath) as f:
        try:
            contents = "".join(f.readlines())
            if pattern.match(contents) != None:
                goodFiles.append((filename, contents))
        except:
            pass

for filename, contents in goodFiles:
    print(colored("----- File: " + join(path, filename) + " -----", "green"))
    print(contents, "\n")
