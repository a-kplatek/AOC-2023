import sys
from dataclasses import dataclass
from typing import Set, List, Any
from functools import reduce

Self = Any


def main(args):
    result = 0


    times = None
    distances = None

    occurances = []

    with open(args[0]) as f:

        for item in f.readlines():
            if item.startswith("Time:      "):
                item = item.replace("Time:      ", "")
                item = item.replace("\n", "")
                times = [int(t) for t in item.split(" ") if t.isdigit()]

            if item.startswith("Distance:  "):
                item = item.replace("Distance:  ", "")
                item = item.replace("\n", "")
                distances = [int(t) for t in item.split(" ") if t.isdigit()]



    for i in range(len(times)):
        distance = distances[i]
        time = times[i]
        partial = 0
        for t in range(time):
            time_left = time - t
            speed = t
            travelled = time_left * speed
            if travelled > distance:
                partial += 1
        print("partial: " + str(partial))
        occurances.append(partial)
        print("occurances: " + str(occurances))


    result = reduce(lambda x, y: x * y, occurances, 1)

    print("times: " + str(times))
    print("distances: " + str(distances))

    print("result: " + str(result))





if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt
