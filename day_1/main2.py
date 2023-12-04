import sys


def main(args):
    result = 0

    # print(args)

    numbers = [str(i) for i  in range(0, 10)]
    other_digits = {
                       "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
                       # "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
    }

    def replace(item: str):

        print("orig: " + item)
        for i in range(len(item)):
            slice = item[:i+1]
            rest = item[i+1:]
            # print("slice: " + slice)
            # print("rest: " + rest)
            for key, value in other_digits.items():
                slice = slice.replace(key, value)
                item = slice + rest

        print("amended: " + item)
        return item

    def b_replace(item: str):
        print("orig: " + item)
        for i in reversed(range(len(item))):
            rest = item[:i+1]
            slice = item[i+1:]
            print("slice: " + slice)
            print("rest: " + rest)
            for key, value in other_digits.items():
                slice = slice.replace(key, value)
                item = rest + slice

        print("amended: " + item)
        return item

    with open(args[0]) as f:

        for item in f.readlines():
            orig_item = replace(item)
            b_item = b_replace(item)

            found = [i for i in orig_item if i in numbers]
            b_found = [i for i in b_item if i in numbers]

            result = result + int(found[0] + b_found[-1])
            print("partial: " + found[0] + b_found[-1])
            print("result: " + str(result))

    print("final: " + str(result))


if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt