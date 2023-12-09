import dataclasses
import sys

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

    i = 0
    steps = 0
    # directions = tree["AAA"]
    directions = [v for k, v in tree.items() if k.endswith("A")]

    print("directions: "+ str(directions))


    while True:

        # print("i: " + str(i))
        instr = instructions[i]
        # print("instr: "+ str(instr))

        # key = directions[LEFT] if instr == "L" else directions[RIGHT]
        keys = [d[LEFT] if instr == "L" else d[RIGHT] for d in directions]


        # print("keys: "+ str(keys))

        directions = [tree[key] for key in keys]

        # print("directions: "+ str(directions))

        if i < len(instructions)-1:
            i += 1
        else:
            i = 0

        steps += 1


        # if key == "ZZZ":
        if all([key.endswith("Z") for key in keys]):
            break

        if steps % 1000000 == 0:
            print(steps)

    print(steps)

if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt
