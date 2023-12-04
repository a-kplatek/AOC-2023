import sys
from typing import List

NUMBERS = [str(i+1) for i in range(9)]
DOT = "."

def is_symbol(s):
    return s not in NUMBERS + [DOT]

def replace(x: int, y: int, data: List[List[str]]):

    movements = [(0, -1), (1, -1), (-1, 0), (1, 0), (0, 1), (-1, 1), (-1, -1), (1, 1)]

    max_x = len(data) - 1
    max_y = len(data[0]) - 1

    # print("x:", x, " y:", y)
    # print("data :" + str(data))

    if is_symbol(data[x][y]) or data[x][y] == "0":
        for dx, dy in movements:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and nx <= max_x and ny >= 0 and ny <= max_y:
                if data[nx][ny] in NUMBERS:
                    data[nx][ny] = "0"


def replacer(data: List[List[str]]):
    for x, row in enumerate(data):
        for y, item in enumerate(row):
                print("x:", x, " y:", y)
                replace(x, y, data)

def main(args):
    result = []
    data = []
    final_sum = 0
    with open(args[0]) as f:
        for item in f.readlines():
            data.append([i for i in item][:-1])

    for i in range(10):
        replacer(data)

    print(data)

    for row in data:
        result.append(curr:= [i for i in row if i in NUMBERS])
        if curr:
            final_sum += int("".join(curr))

    print(result)
    print(final_sum)

if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt