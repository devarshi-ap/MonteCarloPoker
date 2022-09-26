import random
from hands import *
from utils import *
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
        self.villains = []       # varying # of villains (2 cards/villain)
        self.build(deck)

    def build(self, deck):
        # deal 2 cards to hole, 2x to x villains, and 5 to community (naive post-flop)
        for i in range(2):
            self.hole.append(deck.deal())

        for i in range(random.randint(1, 5)):
            for k in range(2):
                self.villains.append(deck.deal())

        for i in range(5):
            self.community.append(deck.deal())

    def print_table(self):
        hole_strArr = []
        community_strArr = []
        villain_strArr = []

        for card in self.hole:
            hole_strArr.append("{value}{suit}".format(value=card[0], suit=SUITS_MAP.get(card[1])))
        print("Hole: ", ' '.join(hole_strArr))

        for card in self.villains:
            villain_strArr.append("{value}{suit}".format(value=card[0], suit=SUITS_MAP.get(card[1])))
        print("Villains: ", ', '.join(villain_strArr))

        for card in self.community:
            community_strArr.append("{value}{suit}".format(value=card[0], suit=SUITS_MAP.get(card[1])))
        print("Community: ", ', '.join(community_strArr))

    def get_table(self):
        return self.hole + self.community

    def get_villains_hands(self):
        villains_hands = []
        for i in range(0, len(table.villains), 2):
            temp_villain_hand = [table.villains[i], table.villains[i + 1]] + table.community
            villains_hands.append(classify(temp_villain_hand))
        return villains_hands

def classify(hand):
    if check_royal_flush(hand)[0]:
        return "Royal Flush"
    elif check_straight_flush(hand)[0]:
        return 'Straight Flush'
    elif check_four_of_kind(hand)[0]:
        return 'Fours'
    elif check_full_house(hand)[0]:
        return 'Full House'
    elif check_flush(hand)[0]:
        return 'Flush'
    elif check_straight(hand)[0]:
        return 'Straight'
    elif check_three_of_kind(hand)[0]:
        return 'Threes'
    elif check_two_pair(hand)[0]:
        return 'Two Pairs'
    elif check_pair(hand)[0]:
        return 'One Pair'
    else:
        return 'High Card'

def game_result(player_hand, villain_hands):
    player_quantified = HAND_RANK_MAP.get(player_hand)
    villains_quantified = [HAND_RANK_MAP.get(villain) for villain in villain_hands]
    return "Win" if player_quantified > max(villains_quantified) else "Lose" if player_quantified < max(villains_quantified) else "Draw"

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
    results_count = {
        "Win": 0,
        "Lose": 0,
        "Draw": 0
    }
    NUM_SIMULATIONS = int(input("# Simulations: "))
    print("\n🔮 Poker Monte-Carlo Simulator\n\t>>>> running %s simulations...\n-------------------------------\n" % NUM_SIMULATIONS)

    for i in range(NUM_SIMULATIONS):
        deck = Deck()
        table = Table(deck)
        # table.print_table()
        hand = table.get_table()

        my_hand = classify(hand)
        hand_count[my_hand] += 1

        villains_hands = table.get_villains_hands()

        results_count[game_result(my_hand, villains_hands)] += 1

    # Connect to DB
    connection = sqlite3.connect("poker.db")
    cursor = connection.cursor()

    # Create Table
    cursor.execute("CREATE TABLE IF NOT EXISTS Poker (Hand text, Count number)")
    cursor.execute("CREATE TABLE IF NOT EXISTS GameResults (Result text, Count number)")

    # Make sure Table is Clear
    cursor.execute('DELETE FROM Poker;', )
    cursor.execute('DELETE FROM GameResults;', )

    # Insert Hand Map to DB
    for hand in hand_count:
        cursor.execute("INSERT OR IGNORE INTO Poker VALUES ('{hand_name}', {hand_count})".format(hand_name=hand, hand_count=hand_count[hand]))

    # Insert Game Results to DB
    for result in results_count:
        cursor.execute("INSERT OR IGNORE INTO GameResults VALUES ('{result_name}', {result_count})".format(result_name=result, result_count=results_count[result]))

    # Print Records
    for row in cursor.execute("SELECT * FROM Poker"):
        print(row)

    print('\n')

    for row in cursor.execute("SELECT * FROM GameResults"):
        print(row)

    connection.commit()

    connection.close()
