import random
from utils import *
from hands import *

"""
Test with PyTest
"""

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    # build deck as array of card-tuples [('A', 's'), ...]
    def build(self):
        for value in RANKS:
            for suit in SUITS:
                self.cards.append((value, suit))

    # shuffle array of card-tuples
    def shuffle(self):
        random.shuffle(self.cards)

    # pop card-tuple from top of deck
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop()

class Table:
    def __init__(self, deck):
        self.community = []     # 5 cards
        self.hole = []          # 2 cards
        self.build(deck)

    def build(self, deck):
        # deal 2 cards to hole and 5 to community (naive post-flop)
        for i in range(2):
            self.hole.append(deck.deal())
        for i in range(5):
            self.community.append(deck.deal())

    def print_table(self):
        hole_strArr = []
        community_strArr = []

        for card in self.hole:
            hole_strArr.append("{value}{suit}".format(value=card[0], suit=SUITS_MAP.get(card[1])))
        print("Hole: ", ' '.join(hole_strArr))

        for card in self.community:
            community_strArr.append("{value}{suit}".format(value=card[0], suit=SUITS_MAP.get(card[1])))
        print("Community: ", ', '.join(community_strArr))

    def get_table(self):
        return self.hole + self.community

if __name__ == '__main__':
    deck = Deck()
    table = Table(deck)
    table.print_table()

    hand = table.get_table()
    print(hand)

    pairs = check_pair(hand)
    print("\n--------------------------------\n\n# Pairs\t\t: ", len(pairs))
    # print(format_cards(pairs) if len(pairs) > 0 else "")

    two_pairs = check_two_pair(hand)
    print("# 2 Pairs\t: ", len(two_pairs))
    # print(two_pairs)

    threes = check_three_of_kind(hand)
    print("# Three of a Kind\t: ", len(threes))
    # print(threes)

    straights = check_straight(hand)
    print("# Straights\t: ", len(straights))
    # print(straights)

    flushes = check_flush(hand)
    print("# Flushes\t: ", len(flushes))
    # print(flushes)

    full_houses = check_full_house(hand)
    print("# Full Houses\t: ", len(full_houses))
    # print(full_houses)

    fours = check_four_of_kind(hand)
    print("# Fours\t: ", len(fours))
    # print(fours)

    straight_flushes = check_straight_flush([('A', 'd'), ('2', 'd'), ('3', 'd'), ('4', 'd'), ('5', 'd'), ('8', 'h'), ('7', 's')])
    print("# Straight Flushes\t: ", len(straight_flushes))
    # print(straight_flushes)