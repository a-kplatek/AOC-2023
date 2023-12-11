import sys
from typing import List, Tuple


def expand_rows(input: List[List[str]]) -> List[List[str]]:
    extented = []
    for row in (input):
        extented.append(row)
        if all([item in [".", "X"] for item in row]):
            extented.append(
                len(row) * ["X"]
            )

    return extented


def transpose(x: List[List[str]]) -> List[List[str]]:
    return (
        [[x[rowix][colix] for rowix in (range(len(x)))] for colix in (range(len(x[0])))]
    )


assert transpose(
    [[1, 2], [11, 22], [33, 44]]
) == [[1, 11, 33], [2, 22, 44]]


def expand_columns(input: List[List[str]]) -> List[List[str]]:
    trans1 = (transpose(input))
    rows = (expand_rows(trans1))
    return transpose(rows)


def expand_all(input):
    rows = (expand_columns(input))
    return expand_rows(rows)


def find_galaxies(universe: List[List[str]]) -> List[Tuple[int, int]]:
    return [
        shifter(universe, (x, y)) for x, row in (enumerate(universe)) for y, item in (enumerate(row)) if item == "#"
    ]


def shifter(universe: List[List[str]], coord: Tuple[int, int]) -> Tuple[int, int]:
    # SHIFT = 999_999
    SHIFT = 1000000 - 2  # because I added one instead of multiplying

    yshift = sum([x == "X" for ix, x in enumerate(universe[coord[0]]) if ix < coord[1]])
    xshift = sum([x == "X" for ix, x in enumerate([row[coord[1]] for row in (universe)]) if ix < coord[0]])

    return (
        coord[0] + xshift * SHIFT,
        coord[1] + yshift * SHIFT,
    )


print(
    find_galaxies(
        [
            # 0    1    2
            [".", ".", "#"],  # 0
            [".", ".", "."],  # 1
            [".", "#", "."],  # 2
            [".", ".", "."],  # 3
            ["#", ".", "."],  # 4
        ]
    )
)

assert find_galaxies(
    [
        # 0    1    2
        [".", ".", "#"],  # 0
        [".", ".", "."],  # 1
        [".", "#", "."],  # 2
        [".", ".", "."],  # 3
        ["#", ".", "."],  # 4
    ]
) == [(0, 2), (2, 1), (4, 0)]


def combinations(galaxy_coord: List[Tuple[int, int]]) -> List[Tuple[Tuple[int, int]]]:
    return [
        (a, b) for ixa, a in (enumerate(galaxy_coord)) for ixb, b in (enumerate(galaxy_coord)) if
        ixa > ixb
    ]


print("combi")
print(combinations(
    [
        (1, 2),
        (3, 4),
        (5, 6),
    ]
))

# ) == {
#     {(1, 2), (3, 4)},
#     {(1, 2), (5, 6)},
#     {(5, 6), (3, 4)},
#
# }

from math import fabs


def distance(a, b):
    component1 = max(
        fabs(a[0] - b[0]),
        fabs(a[1] - b[1])
    )
    component2 = min(
        fabs(a[0] - b[0]),
        fabs(a[1] - b[1])
    )

    return component1 + component2


print(distance((1, 2), (5, 5)))


# assert distance(
#     (1, 2),
#     (5, 5)
# ) == 4 + 1


def print_matrix(name, m):
    print(f"{name}:")
    for row in m:
        print(row)


print_matrix("expand_columns", expand_columns(
    [
        [".", ".", "."],
        ["*", ".", "."],
        [".", ".", "."],
        ["*", ".", "."],
        [".", ".", "."],
    ]
))


def main(args):
    input = []
    with open(args[0]) as f:
        for ix, item in enumerate(f.readlines()):
            input.append([i for i in item if i != "\n"])

    print_matrix("input", input)

    # expanded = expand_all(input)
    # print_matrix("expanded", expanded)

    erows = expand_rows((input))
    print_matrix("expand_rows", erows)
    # print_matrix("expand_columns", expand_columns(input))

    expanded = expand_columns((erows))
    print_matrix("expanded", expanded)

    galaxies = find_galaxies(expanded)
    print("galaxies: " + str(galaxies))

    combi = combinations(galaxies)
    print("combi: " + str(len(combi)))

    result = sum(
        [distance(a, b) for a, b in combi]
    )
    print("result : " + str(
        result
    ))


if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt
