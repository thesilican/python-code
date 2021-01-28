import random
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from math import floor


def experiment():
    return np.sum(np.random.rand(262) < 0.05)


x = np.array([np.sum(np.random.rand(262) < 0.05) for _ in range(10_000)])

print("Done")

for i in range(10000):
    np.random.seed(10)
    size = floor(1.1**i)
    if size > len(x):
        break
    plt.hist(x[:size], bins=np.arange(0, 31))
    plt.title(f"{size} datapoints")
    plt.savefig("fig.png")
    sleep(0.1)
