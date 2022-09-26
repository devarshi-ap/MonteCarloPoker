import random
from utils import *
from hands import *
import sqlite3

"""
Test with PyTest

Monte Carlo simulation to get an approximation to poker hand probabilities. Use > 1 million randomly generated hands
1) Deal out 7 card hands
2) Classify hand
3) Save to DB
4) Use DB entries to evaluate the probability of different hands
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
    hand_count = {
        'High Card': 0,
        'One Pair': 0,
        'Two Pairs': 0,
        'Threes': 0,
        'Straight': 0,
        'Flush': 0,
        'Full House': 0,
        'Fours': 0,
        'Straight Flush': 0,
        'Royal Flush': 0,
    }
    NUM_SIMULATIONS = 100

    for i in range(NUM_SIMULATIONS):
        deck = Deck()
        table = Table(deck)
        # table.print_table()
        hand = table.get_table()
        # print("\nRaw Hand: ", hand)

        hand_count[classify(hand)] += 1
        # print("\n--------------------------------\n\nOverall Hand \t: ", classify(hand))

    # print(hand_count)

    # Connect to DB
    connection = sqlite3.connect("poker.db")
    cursor = connection.cursor()

    # Create Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Poker
                        (Hand text, Count number)''')

    # Make sure Table is Clear
    cursor.execute('DELETE FROM Poker;', );

    # Insert Hand Map to DB
    for hand in hand_count:
        cursor.execute("INSERT OR IGNORE INTO Poker VALUES ('{hand_name}', {hand_count})".format(hand_name=hand, hand_count=hand_count[hand]))

    # Print Records
    for row in cursor.execute("SELECT * FROM Poker"):
        print(row)

    connection.commit()

    connection.close()