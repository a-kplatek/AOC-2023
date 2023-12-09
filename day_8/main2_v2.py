import dataclasses
import sys
import math

# @dataclasses.dataclass
# class Tree:
#     name: str




def main(args):

    instructions = []
    tree = {}
    LEFT = 0
    RIGHT = 1

    with open(args[0]) as f:
        for ix, item in enumerate(f.readlines()):
            if ix == 0:
                instructions = [i for i in item if i != "\n"]

            if ix > 1:
                #AAA = (BBB, CCC)
                mapping = str.maketrans("\n()", "   ")
                item = item.translate(mapping)
                item = item.replace(" ", "")

                k, raw_v = tuple(item.split("="))
                left, right = tuple(raw_v.split(","))
                tree[k] = (left, right)

    print(tree)

    results = set()



    for directions in [v for k, v in tree.items() if k.endswith("A")]:
        i = 0
        steps = 0
        while True:

            # print("i: " + str(i))
            instr = instructions[i]
            # print("instr: "+ str(instr))

            key = directions[LEFT] if instr == "L" else directions[RIGHT]

            print("key: "+ str(key))

            directions = tree[key]

            print("directions: "+ str(directions))

            if i < len(instructions)-1:
                i += 1
            else:
                i = 0

            steps += 1

            if key.endswith("Z"):
                results.add(steps)
                break

    print(math.lcm(*results))

if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt
