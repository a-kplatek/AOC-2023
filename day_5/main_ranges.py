import sys
from dataclasses import dataclass
from typing import List, Tuple

from tqdm import tqdm


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


# optimized version

def move_range(initial: List[Tuple[int, int]], move_specs: List[MoveSpec]) -> List[Tuple[int, int]]:
    result = []

    # print("initial : " + str(initial))
    # print("move_specs : " + str(sorted(move_specs, key = lambda key: key.source_lower_bound)))

    for start, end in initial:
        # last_handled_start = start
        # end = start + offset - 1
        # print("start: " + str(start))
        # print("end: " + str(end))

        partial_results = []
        for spec in sorted(move_specs, key=lambda key: key.source_lower_bound):

            spec_start = spec.source_lower_bound
            spec_end = spec.source_upper_bound

            # print("spec_start: " + str(spec_start))
            # print("spec_end: " + str(spec_end))

            left = max(start, spec_start)
            right = min(end, spec_end)

            # print("left: " + str(left))
            # print("right: " + str(right))

            if left < right:
                if start < left - 1:
                    partial_results.append(
                        (start, left - 1),
                    )
                offset = start - spec_start
                partial_results.append(
                    (spec.destination_start + offset, spec.destination_start + right - left + offset - 1),
                )
                start = right + 1

            # print("partial_results: " + str(partial_results))

        if not partial_results:
            partial_results = [(start, end)]

        result.extend(partial_results)

    return result


def plan_range(initial, iterations: List[List[MoveSpec]]):
    for move_specs in tqdm(iterations):
        print("initial: " + str(initial))
        print("move_specs: " + str(move_specs))
        initial = move_range(initial, move_specs)

    return min(
        [start for start, offset in initial if start]
    )


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
                    (start, start + offset)
                    for start, offset
                    in zip(raw[::2], raw[1::2])
                ]

            if len(item.split(" ")) == 3:
                d, s, r = tuple([int(i) for i in item.split(" ") if i != "\n"])
                move_specs.append(
                    MoveSpec(
                        destination_start=d,
                        source_lower_bound=s,
                        source_upper_bound=s + r - 1
                    )
                )

            if item.endswith("map:\n"):
                if move_specs:
                    iterations.append(move_specs)
                move_specs = []

        iterations.append(move_specs)

    print("ranges : " + str(ranges))
    print("iterations : " + str(iterations))

    result = plan_range(
        ranges,
        iterations
    )

    print("result : " + str(
        result
    ))



if __name__ == '__main__':
    main(sys.argv[1:])
