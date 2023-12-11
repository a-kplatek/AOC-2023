import sys
from typing import List, Tuple

sys.setrecursionlimit(100000)

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)

ALLOWED_MOVES = {
    "|": [N, S],
    "-": [E, W],
    "L": [N, E],
    "J": [N, W],
    "7": [S, W],
    "F": [S, E],
}

START = "S"
GROUND = "."

MOVES = [N, S, E, W]


def find_start(input: List[List[str]]) -> Tuple[int, int]:
    for y, row in enumerate(input):
        for x, char in enumerate(row):
            if char == START:
                return x, y


HISTORY = []


def is_move_happened(start: Tuple[int, int], dest: Tuple[int, int]) -> bool:
    if (dest, start) in HISTORY or (start, dest) in HISTORY:
        return True
    else:
        HISTORY.append((dest, start))
        return False


def determine_start():
    return "J"


def print_matrix(name, m):
    print(f"{name}:")
    for row in m:
        print(row)


def flood(input: List[List[str]], current_map: List[List[int]], start: Tuple[int, int]) -> List[List[int]]:
    current_mark = input[start[1]][start[0]]

    if current_mark == START:
        current_mark = determine_start()

    moves = ALLOWED_MOVES.get(current_mark, [])

    for move in moves:
        dest = (start[0] + move[0], start[1] + move[1])
        # print("start: " + str(start))
        # print("move: " + str(move))
        # print("dest: " + str(dest))
        # print_matrix("input", input)
        if not is_move_happened(start, dest):
            # print("cond met")
            # print_matrix("current_map", current_map)
            try:
                current_map[dest[1]][dest[0]] = current_map[start[1]][start[0]] + 1
                current_map = flood(input, current_map, dest)
            except IndexError:
                continue
        # else:
        # print("cond NOT met")

    return current_map


def main(args):
    input = []
    with open(args[0]) as f:
        for ix, item in enumerate(f.readlines()):
            input.append([i for i in item if i != "\n"])

    print("input: " + str(input))

    current_map = [[0 for _ in row] for row in input]
    print_matrix("current_map", current_map)

    start = find_start(input)

    print("start: " + str(start))

    # current_map[start[1]][start[0]] = 0
    current_map = flood(input, current_map, start)

    print_matrix("current_map", current_map)

    result = max(map(lambda i: max(i), current_map))
    print("result : " + str(
        result / 2
    ))


if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt
