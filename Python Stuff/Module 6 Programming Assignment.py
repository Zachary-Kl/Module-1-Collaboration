import multiprocessing
import os
import time
import random

def proc():
    time.sleep(random.uniform(0,1))
    print(time.strftime("%H-%M-%S"))

if __name__ == "__main__":
    for n in range(3):
        p = multiprocessing.Process(target=proc)
        p.start()