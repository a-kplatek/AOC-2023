import sys
from typing import List, Tuple

import tqdm


def expand_rows(input: List[List[str]]) -> List[List[str]]:
    extented = []
    for row in tqdm.tqdm(input):
        extented.append(row)
        if all([item == "." for item in row]):
            extented.append(row)

    return extented


# assert expand_rows(
#     [
#         [".", "."],
#         ["*", "."],
#         [".", "."],
#         ["*", "."],
#         [".", "."],
#     ]
# ) == [
#            [".", "."],
#            [".", "."],
#            ["*", "."],
#            [".", "."],
#            [".", "."],
#            ["*", "."],
#            [".", "."],
#            [".", "."],
#        ]


def transpose(x: List[List[str]]) -> List[List[str]]:
    return (
        [[x[rowix][colix] for rowix in tqdm.tqdm(range(len(x)))] for colix in tqdm.tqdm(range(len(x[0])))]
    )


assert transpose(
    [[1, 2], [11, 22], [33, 44]]
) == [[1, 11, 33], [2, 22, 44]]


def expand_columns(input: List[List[str]]) -> List[List[str]]:
    return transpose(expand_rows(transpose(
        input
    )))


def expand_all(input):
    return expand_columns(expand_rows(input))


# assert expand_columns(
#     [
#         [".", ".", "."],
#         ["*", ".", "."],
#         [".", ".", "."],
#         ["*", ".", "."],
#         [".", ".", "."],
#     ]
# )


def find_galaxies(universe: List[List[str]]) -> List[Tuple[int, int]]:
    return [
        (x, y) for x, row in tqdm.tqdm(enumerate(universe)) for y, item in tqdm.tqdm(enumerate(row)) if item == "#"
    ]


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
        (a, b) for ixa, a in tqdm.tqdm(enumerate(galaxy_coord)) for ixb, b in tqdm.tqdm(enumerate(galaxy_coord)) if
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


def main(args):
    input = []
    with open(args[0]) as f:
        for ix, item in enumerate(f.readlines()):
            input.append([i for i in item if i != "\n"])

    print_matrix("input", input)

    expanded = expand_all(input)
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
