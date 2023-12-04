import sys
from dataclasses import dataclass
from typing import Set, List, Any


@dataclass
class Card:
    id: int
    winning_numbers: Set[int]
    my_numbers: Set[int]

    @staticmethod
    def _parse_card(raw: str) -> Set[int]:
        raw = raw.replace("  ", " ")
        return set([int(item) for item in raw.split(" ") if item != ""])

    @staticmethod
    def from_string(raw: str):
        card_id, rest = tuple(raw.split(": "))
        card_id = card_id.replace("Card ", "")
        raw_left, raw_right = tuple(rest.split(" | "))

        return Card(
            id=int(card_id),
            winning_numbers=Card._parse_card(raw_left),
            my_numbers=Card._parse_card(raw_right)
        )

    def points(self):
        quantity = len(self.winning_numbers & self.my_numbers)

        if quantity == 0:
            return 0

        result = 1

        for i in range(1, quantity + 1):
            result = 2 * result

        print("card: " + str(self) + " has " + str(result))

        return int(result / 2)

    def matching(self):
        return len(self.winning_numbers & self.my_numbers) + 1

    def points_v2(self, index: int, game: List[Any]) -> int:
        # del game[0]
        total = 1
        for ix in range(self.matching() - 1):
            if ix < len(game):
                # print("card: " + str(self))
                # print("index: " + str(index))
                # print("ix: " + str(ix))
                total += game[index + ix + 1].points_v2(index + ix + 1, game)

        return total


def main(args):
    result = 0
    game = []
    with open(args[0]) as f:
        for item in f.readlines():
            card = Card.from_string(item)
            game.append(card)

    for index, item in enumerate(game):
        print("card: " + str(item))
        print("index: " + str(index))
        result += item.points_v2(index, game)

    print("final: " + str(result))


if __name__ == '__main__':
    main(sys.argv[1:])

# USAGE: python main.py input.txt
