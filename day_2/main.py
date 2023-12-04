import sys
from dataclasses import dataclass
from typing import List

# 12 red cubes, 13 green cubes, and 14 blue cubes

MAX_GREEN = 13
MAX_RED = 12
MAX_BLUE = 14

@dataclass
class Subset:
    red: int = 0
    green: int = 0
    blue: int = 0

    def is_valid(self):
        print(self.red)
        print(self.green)
        print(self.blue)
        self.green <= MAX_GREEN
        return self.red <= MAX_RED and self.green <= MAX_GREEN and self.blue <= MAX_BLUE

    @staticmethod
    def from_string(raw_subset: str):
        red = 0
        green = 0
        blue = 0
        cube_pairs = raw_subset.split(", ")
        print("cube_pairs: " + str(cube_pairs))
        for cube_pair in cube_pairs:
            value, color = tuple(cube_pair.split(" "))
            color = color.replace("\n", "")
            if color == "red":
                red = int(value)
            if color == "green":
                green = int(value)
            if color == "blue":
                blue = int(value)
            print(
                    "subset: " + str(Subset(
                    red, green, blue
                ))
            )
        return(
            Subset(
                red, green, blue
            )
        )


@dataclass
class Game:
    id: int
    subsets: List[Subset]

    def is_valid(self):
        return all(
            [subset.is_valid() for subset in self.subsets]
        )

    @staticmethod
    def from_string(raw: str):
        game_id, rest = tuple(raw.split(": "))
        game_id = game_id.replace("Game ", "")
        tmp = []
        subsets = rest.split("; ")
        for subset in subsets:
            tmp.append(Subset.from_string(subset))
        return(
            Game(int(game_id), tmp)
        )

def main(args):
    result = 0
    with open(args[0]) as f:
        for item in f.readlines():
            game = Game.from_string(item)
            if game.is_valid():
                print("game.id " + str(game.id) + " is valid")
                result = result + game.id


    print("final: " + str(result))


if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt