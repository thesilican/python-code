def getPascalsTriangle(maxLevel: int):
    index = 1
    triangle = [1]
    ret = [triangle]
    while index <= maxLevel:
        newTriangle = []
        for i in range(len(triangle) + 1):
            if i == 0 or i == len(triangle):
                newTriangle.append(1)
            else:
                newTriangle.append(triangle[i] + triangle[i - 1])
        triangle = newTriangle
        index += 1
        ret.append(triangle)
        # DEBUG MODE ONLY
        ret = []
    return ret


import time
import threading
import multiprocessing
import sys
import datetime


lock = multiprocessing.Lock()


def doRun(i):
    def inner():
        print(str(datetime.datetime.now()).split()[1] + " Start " + str(i))
        start = time.perf_counter()
        getPascalsTriangle(i)
        end = time.perf_counter()
        with lock:
            f = open("out.csv", "a")
            try:
                f.write("{:d},{:.6f}\n".format(i, end - start))
            finally:
                f.close()  # try close in any circumstances if open passed
        print(str(datetime.datetime.now()).split()[1] + " Finish " + str(i))
    return inner

print(str(datetime.datetime.now()).split()[1] + " Start Program")
for i in range(1, 5000 + 1, 10):
    threading.Thread(target=doRun(i)).start()
print(str(datetime.datetime.now()).split()[1] + " Finish Creating Threads")
