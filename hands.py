"""
Royal Flush
Straight Flush
4 of a Kind
Full House
Flush
✅ wStraight
✅ 3 of a Kind
✅ 2 Pair
✅ Pair
High Card

All below functions:
    @param: 7-card hand list of tuples
    @return: [varies]
"""
from utils import *

def format_cards(cards):
    cards_strArr = []
    for group in cards:
        temp_arr = []
        for card in group:
            temp_arr.append("{value}{suit}".format(value=card[0], suit=SUITS_MAP.get(card[1])))
        cards_strArr.append(temp_arr)
    return cards_strArr

def check_pair(hand):
    pairs = []
    for x in range(len(hand)):
        for y in range(x + 1, len(hand)):
            if hand[x][0] == hand[y][0]:
                # print(hand[x], hand[y])
                pairs.append((hand[x], hand[y]))
    return pairs

def check_two_pair(hand):
    two_pairs = []
    pairs = check_pair(hand)
    for pair1 in range(len(pairs)):
        for pair2 in range(pair1 + 1, len(pairs)):
            if pairs[pair1][0][0] != pairs[pair2][0][0]:
                two_pairs.append((pairs[pair1], pairs[pair2]))
    return two_pairs

def check_three_of_kind(hand):
    hand_values = [card[0] for card in hand]
    threes = []
    for value in hand_values:
        if hand_values.count(value) == 3 and value not in threes:
            threes.append(value)
    return threes

def check_straight(hand):
    num_straights = 0
    straights = []
    hand_values = []
    for card in hand:
        if RANKS_MAP.get(card[0]) not in hand_values:
            hand_values.append(RANKS_MAP.get(card[0]))
    # Ace is both 14 and 1
    if 1 in hand_values:
        hand_values.append(14)
    hand_values.sort()
    if len(hand_values) > 5:
        for i in range(0, len(hand_values)-4):
            if hand_values[i] == hand_values[i+1]-1 == hand_values[i+2]-2 == hand_values[i+3]-3 == hand_values[i+4]-4:
                straights.append(hand_values[i:i+4])
                num_straights += 1
    return straights

