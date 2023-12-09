import sys
from copy import copy
from typing import List


def diff(input: List[int]) -> List[int]:
    return [
        n - p
        for n, p
        in zip(input[1:], input[:-1])
    ]


assert diff([1, 3, 6, 10, 15, 21]) == [2, 3, 4, 5, 6]


def build_tree_till_zeros(input: List[int]) -> List[List[int]]:
    result = []
    result.append(input)
    partial = copy(input)
    while True:
        partial = diff(partial)
        result.append(partial)
        if sum(partial) == 0:
            return result


assert build_tree_till_zeros([1, 3, 6, 10, 15, 21]) == (tree := [
    [1, 3, 6, 10, 15, 21],
    [2, 3, 4, 5, 6],
    [1, 1, 1, 1],
    [0, 0, 0],
])


def history_value(tree: List[List[int]]) -> int:
    last_elements_reversed = list(reversed(
        [row[-1] for row in tree]
    ))
    result = 0
    for i in range(len(tree)):
        result = last_elements_reversed[i] + result

    return result


assert history_value(tree) == 28

assert history_value(build_tree_till_zeros([0, 3, 6, 9, 12, 15])) == 18
assert history_value(build_tree_till_zeros([1, 3, 6, 10, 15, 21])) == 28
print((build_tree_till_zeros([10, 13, 16, 21, 30, 45])))
print(history_value(build_tree_till_zeros([10, 13, 16, 21, 30, 45])))
assert history_value(build_tree_till_zeros([10, 13, 16, 21, 30, 45])) == 68


def prev_history_value(tree: List[List[int]]) -> int:
    last_elements_reversed = list(reversed(
        [row[0] for row in tree]
    ))
    result = 0
    for i in range(len(tree)):
        result = last_elements_reversed[i] - result

    return result


assert prev_history_value(
    build_tree_till_zeros(
        [10, 13, 16, 21, 30, 45]
    )
) == 5


def main(args):
    input = []
    with open(args[0]) as f:
        for ix, item in enumerate(f.readlines()):
            input.append([int(i) for i in item.split(" ") if i != "\n"])

    result = sum(
        [
            prev_history_value(build_tree_till_zeros(i))
            for i
            in input
        ]
    )

    print("result : " + str(
        result
    ))


if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt
