import sys


def main(args):
    result = 0

    # print(args)

    numbers = [str(i) for i  in range(0, 10)]

    with open(args[0]) as f:

        for item in f.readlines():
            found = [i for i in item if i in numbers]
            result = result + int(found[0] + found[-1])
            print(result)

    print(result)


if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt