import sys
from collections import Counter

card_powers = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 0
}


def card_hand_helper(card: str) -> int:
    counter = Counter(card)
    if len(counter) == 1:  # Five of a kind
        return 7
    elif len(counter) == 2 and max(counter.values()) == 4:  # Four of a kind
        return 6
    elif len(counter) == 2 and max(counter.values()) == 3:  # Full house
        return 5
    elif len(counter) == 3 and max(counter.values()) == 3:  # Three of a kind
        return 4
    elif len(counter) == 3 and max(counter.values()) == 2:  # Two pair
        return 3
    elif len(counter) == 4:  # One pair
        return 2
    else:
        return 1


def card_hand(card: str) -> int:
    return max(
        [card_hand_helper(card.replace("J", i)) for i in card_powers.keys() if i != "J"]
    )


assert card_hand("AAAAA") == 7
assert card_hand("AA8AA") == 6
assert card_hand("23332") == 5
assert card_hand("TTT98") == 4
assert card_hand("23432") == 3
assert card_hand("A23A4") == 2
assert card_hand("23456") == 1


def main(args):
    cards = []
    bids = []

    as_tuple_list = []

    with open(args[0]) as f:
        for item in f.readlines():
            # 32T3K 765
            card, bid = tuple(item.split(" "))
            cards.append(card)
            bids.append(int(bid))

    print("cards: " + str(cards))
    print("bids: " + str(bids))

    for c, b in zip(cards, bids):
        as_tuple_list.append(
            (
                card_hand(c),
                card_powers[c[0]],
                card_powers[c[1]],
                card_powers[c[2]],
                card_powers[c[3]],
                card_powers[c[4]],
                b)
        )

    print(as_tuple_list)

    srt = sorted(as_tuple_list)
    scores = [(rank + 1) * power[6] for rank, power in enumerate(srt)]
    score = sum(scores)

    print(score)


if __name__ == '__main__':
    main(sys.argv[1:])
