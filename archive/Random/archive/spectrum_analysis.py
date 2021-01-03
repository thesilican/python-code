FILENAME = "spectrum_clarinet"

f = open(FILENAME + ".txt", "r")
w = open(FILENAME + ".csv", "w")

for line in f.readlines():
  w.write(line.replace("\t", ",") + "\n")

f.close()
w.close()