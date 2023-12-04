import sys
from typing import List
from copy import deepcopy

NUMBERS = [str(i) for i in range(10)]
DOT = "."
ZERO = "0"
WILDCARD = "*"




def aggregate(data: List[List[str]], refined: List[List[str]]) -> int:
    total = 0
    for row_ix, row in enumerate(data):
        for col_ix, item in enumerate(row):
            if item == WILDCARD:

                movements = [(0, -1), (1, -1), (-1, 0), (1, 0), (0, 1), (-1, 1), (-1, -1), (1, 1)]

                max_x = len(data) - 1
                max_y = len(data[0]) - 1

                temp = set()

                for dx, dy in movements:
                    nx = row_ix + dx
                    ny = col_ix + dy
                    if nx >= 0 and nx <= max_x and ny >= 0 and ny <= max_y:
                        # print("added: " + str(refined[nx][ny]))
                        if refined[nx][ny] > 0:
                            temp.add(refined[nx][ny])
                            refined[nx][ny] = 0

                    # print("temp: " + str(temp))

                if len(temp) == 2:
                    as_list = list(temp)
                    print("as list: " + str(as_list))
                    total += (as_list[0] * as_list[1])


    return total



def refine(data: List[List[str]], refined: List[List[str]]):
    for row_ix, row in enumerate(data):
        row_sum = 0
        multiplier = 1
        current_row_sum = 0

        for col_ix, item in enumerate(reversed(row)):

            print("item: "+ item)
            print("row_ix: "+ str(row_ix))
            print("col_ix: "+ str(col_ix))

            if item in NUMBERS:
                # if current_row_sum == 0:
                current_row_sum += int(item) * multiplier
                multiplier *= 10
            else:
                row_sum += current_row_sum
                multiplier = 1

                if current_row_sum < 10:
                    refined[row_ix][len(row) - col_ix - 1] = current_row_sum
                elif current_row_sum < 100:
                    refined[row_ix][len(row) - col_ix - 1] = current_row_sum
                    refined[row_ix][len(row) - col_ix + 1 - 1] = current_row_sum
                elif current_row_sum < 1000:
                    refined[row_ix][len(row) - col_ix - 1] = current_row_sum
                    refined[row_ix][len(row) - col_ix + 1 - 1] = current_row_sum
                    refined[row_ix][len(row) - col_ix + 2 - 1] = current_row_sum

                current_row_sum = 0


            if current_row_sum < 10:
                refined[row_ix][len(row) - col_ix - 1] = current_row_sum
            elif current_row_sum < 100:
                refined[row_ix][len(row) - col_ix - 1] = current_row_sum
                refined[row_ix][len(row) - col_ix + 1 - 1] = current_row_sum
            elif current_row_sum < 1000:
                refined[row_ix][len(row) - col_ix - 1] = current_row_sum
                refined[row_ix][len(row) - col_ix + 1 - 1] = current_row_sum
                refined[row_ix][len(row) - col_ix + 2 - 1] = current_row_sum

    # for ix, row in enumerate(refined):
    #     refined[ix] = list(reversed(row))



def main(args):
    data = []
    with open(args[0]) as f:
        for item in f.readlines():
            data.append([i for i in item][:-1])

    refined = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

    refine(data, refined)


    print(data)
    print(refined)

    print(aggregate(data, refined))



if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt