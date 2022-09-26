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

def classify(hand):
    has_pairs = check_pair(hand)[0]
    has_two_pairs = check_two_pair(hand)[0]
    has_threes = check_three_of_kind(hand)[0]
    has_straights = check_straight(hand)[0]
    has_flushes = check_flush(hand)[0]
    has_full_houses = check_full_house(hand)[0]
    has_fours = check_four_of_kind(hand)[0]
    has_straight_flushes = check_straight_flush(hand)[0]
    has_royal_flush = check_royal_flush(hand)[0]

    if has_royal_flush:
        return "Royal Flush"
    elif has_straight_flushes:
        return 'Straight Flush'
    elif has_fours:
        return 'Fours'
    elif has_full_houses:
        return 'Full House'
    elif has_flushes:
        return 'Flush'
    elif has_straights:
        return 'Straight'
    elif has_threes:
        return 'Threes'
    elif has_two_pairs:
        return 'Two Pairs'
    elif has_pairs:
        return 'One Pair'
    else:
        return 'High Card'

if __name__ == '__main__':
    deck = Deck()
    table = Table(deck)
    table.print_table()

    hand = table.get_table()
    print(hand)

    has_pairs, pairs = check_pair(hand)
    print("\n--------------------------------\n\nPair \t\t\t\t: ", has_pairs)
    # print("\n--------------------------------\n\n# Pairs\t\t: ", len(pairs))
    # print(format_cards(pairs) if len(pairs) > 0 else "")

    has_two_pairs, two_pairs = check_two_pair(hand)
    print("Two Pair \t\t\t: ", has_two_pairs)
    # print("# 2 Pairs\t: ", len(two_pairs))
    # print(two_pairs)

    has_threes, threes = check_three_of_kind(hand)
    print("Threes \t\t\t\t: ", has_threes)
    # print("# Three of a Kind\t: ", len(threes))
    # print(threes)

    has_straights, straights = check_straight(hand)
    print("Straights \t\t\t: ", has_straights)
    # print("# Straights\t: ", len(straights))
    # print(straights)

    has_flushes, flushes = check_flush(hand)
    print("Flushes \t\t\t: ", has_flushes)
    # print("# Flushes\t: ", len(flushes))
    # print(flushes)

    has_full_houses, full_houses = check_full_house(hand)
    print("Full Houses \t\t: ", has_full_houses)
    # print("# Full Houses\t: ", len(full_houses))
    # print(full_houses)

    has_fours, fours = check_four_of_kind(hand)
    print("Fours \t\t\t\t: ", has_fours)
    # print("# Fours\t: ", len(fours))
    # print(fours)

    has_straight_flushes, straight_flushes = check_straight_flush(hand)
    print("Straight Flushes \t: ", has_straight_flushes)
    # print("# Straight Flushes\t: ", len(straight_flushes))
    # print(straight_flushes)

    has_royal_flush, royal_flushes = check_royal_flush(hand)
    print("Royal Flushes \t\t: ", has_royal_flush)
    # print("# Royal Flushes\t: ", len(royal_flushes))
    # print(royal_flushes)

    print("\n--------------------------------\n\nOverall Hand \t: ", classify(hand))