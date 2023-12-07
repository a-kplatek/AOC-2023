

import sys


def main(args):
    current_value = 0
    max_value = current_value

    # print(args)

    with open(args[0]) as f:

        for item in f.readlines():
            # print(item)
            if item != "\n":
                current_value += int(item)
            else:
                if max_value < current_value:
                    max_value = current_value

                current_value = 0
            # print(current_value)

    print(max_value)


if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt