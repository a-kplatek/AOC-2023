import sys
from typing import List
from copy import deepcopy

NUMBERS = [str(i) for i in range(10)]
DOT = "."
ZERO = "0"


def is_symbol(s):
    return s not in NUMBERS + [DOT]


def replace(x: int, y: int, data: List[List[str]]):

    movements = [(0, -1), (1, -1), (-1, 0), (1, 0), (0, 1), (-1, 1), (-1, -1), (1, 1)]

    max_x = len(data) - 1
    max_y = len(data[0]) - 1

    # print("x:", x, " y:", y)
    # print("data :" + str(data))

    if is_symbol(data[x][y]): # or data[x][y] == "0":
        for dx, dy in movements:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx <= max_x and ny >= 0 and ny <= max_y:
                if data[nx][ny] in NUMBERS:
                    data[nx][ny] = "X"


def replacer(data: List[List[str]]):
    for x, row in enumerate(data):
        for y, item in enumerate(row):
                # print("x:", x, " y:", y)
                replace(x, y, data)


def aggregate(data: List[List[str]]):
    final_sum = 0
    for row in data:
        row_sum = 0
        multiplier = 1
        current_row_sum = 0

        for item in reversed(row):
            if item in NUMBERS:
                # if current_row_sum == 0:
                current_row_sum += int(item) * multiplier
                multiplier *= 10
                # elif current_row_sum < 10:
                #     current_row_sum += (10 * int(item))
                # elif current_row_sum < 100:
                #     current_row_sum += (100 * int(item))
                # elif current_row_sum < 1000:
                #     current_row_sum += (1000 * int(item))
            else:
                row_sum += current_row_sum
                multiplier = 1
                current_row_sum = 0

        final_sum += (row_sum + current_row_sum)

    return final_sum


def main(args):
    result = []
    data = []
    with open(args[0]) as f:
        for item in f.readlines():
            data.append([i for i in item][:-1])


    orig_data = deepcopy(data)

    for i in range(20):
        replacer(data)

    print(data)
    for row in data:
        print("".join(row))

    final_sum = aggregate(data)
    total = aggregate(orig_data)

    print("final_sum: " + str(final_sum))
    print("total: " + str(total))
    print("total - final_sum: " + str(total - final_sum))

    # too low: 426907

if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt