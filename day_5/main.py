import itertools
import sys
from dataclasses import dataclass
from typing import List, Tuple
from tqdm import tqdm

# Naive approach

def range_gen(ranges: List[Tuple[int, int]]):
    chained = itertools.chain(
        *[
            range(start, start + offset)
            for start, offset in ranges
        ]
    )
    for num in chained:
        yield num


print(list(range_gen([(0, 5), (7, 3)])))
assert list(range_gen([(0, 5), (7, 3)])) == [0, 1, 2, 3, 4, 7, 8, 9]


@dataclass
class MoveSpec:
    destination_start: int
    source_lower_bound: int
    source_upper_bound: int

    def move(self, source_input: int) -> None:
        if self.source_lower_bound <= source_input <= self.source_upper_bound:
            offset = source_input - self.source_lower_bound
            return self.destination_start + offset
        else:
            return None


def move(source, move_specs: List[MoveSpec]):
    for move_spec in move_specs:
        if (move := move_spec.move(source)) is not None:
            return move

    return source


assert move(
    source=79,
    move_specs=(specs := [
        MoveSpec(destination_start=50, source_lower_bound=98, source_upper_bound=98 + 2),
        MoveSpec(destination_start=52, source_lower_bound=50, source_upper_bound=50 + 48),
    ])
) == 81

assert move(source=14, move_specs=specs) == 14
assert move(source=55, move_specs=specs) == 57
assert move(source=13, move_specs=specs) == 13


def move_all(initial, move_specs: List[MoveSpec]):
    for source in tqdm(initial):
        yield move(source, move_specs)


def plan(initial, iterations: List[List[MoveSpec]]):
    for move_specs in tqdm(iterations):
        print("Next iteration")
        initial = move_all(initial, move_specs)

    return min(initial)


def main(args):
    ranges = []
    iterations = []
    move_specs = []

    # seeds: 79 14 55 13
    #
    # seed-to-soil map:
    # 50 98 2   # dest, source, range
    # 52 50 48

    with open(args[0]) as f:
        for ix, item in enumerate(f.readlines()):
            if ix == 0:
                item = item.replace("seeds: ", "")
                raw = [int(i) for i in item.split(" ") if i != "\n"]
                ranges = [
                    (start, offset)
                    for start, offset
                    in zip(raw[::2], raw[1::2])
                ]

            if len(item.split(" ")) == 3:
                d, s, r = tuple([int(i) for i in item.split(" ") if i != "\n"])
                move_specs.append(
                    MoveSpec(
                        destination_start=d,
                        source_lower_bound=s,
                        source_upper_bound=s + r
                    )
                )

            if item.endswith("map:\n"):
                iterations.append(move_specs)
                move_specs = []

    result = plan(
        range_gen(ranges),
        iterations
    )

    print("result : " + str(
        result
    ))


if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt
