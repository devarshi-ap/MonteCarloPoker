"""
Royal Flush
Straight Flush
✅ 4 of a Kind
✅ Full House
✅ Flush
✅ Straight
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
    return [True if len(pairs) > 0 else False, pairs]

def check_two_pair(hand):
    two_pairs = []
    has_pairs, pairs = check_pair(hand)
    for pair1 in range(len(pairs)):
        for pair2 in range(pair1 + 1, len(pairs)):
            if pairs[pair1][0][0] != pairs[pair2][0][0]:
                two_pairs.append((pairs[pair1], pairs[pair2]))
    return [True if len(two_pairs) > 0 else False, two_pairs]

def check_three_of_kind(hand):
    hand_values = [card[0] for card in hand]
    threes = []
    for value in hand_values:
        if hand_values.count(value) == 3 and value not in threes:
            threes.append(value)
    return [True if len(threes) > 0 else False, threes]

def check_straight(hand):
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
                straights.append(hand_values[i:i+5])
    return [True if len(straights) > 0 else False, straights]

def check_flush(hand):
    flushes = []
    hand_suits = {
        's': 0,
        'c': 0,
        'h': 0,
        'd': 0
    }
    for card in hand:
        hand_suits[card[1]] += 1
    for suit in hand_suits.keys():
        if hand_suits[suit] == 5:
            flushes.append([card for card in hand if card[1] == suit])
    return [True if len(flushes) > 0 else False, flushes]

def check_full_house(hand):
    full_house = []
    hand_values = [RANKS_MAP.get(card[0]) for card in hand]

    for value1 in range(len(hand_values)):
        for value2 in range(value1+1, len(hand_values)):
            if hand_values.count(hand_values[value1]) == 3 and hand_values.count(hand_values[value2]) == 2 and hand_values[value1] != hand_values[value2]:
                full_house.append((3 * [hand_values[value1]], 2 * [hand_values[value2]]))
                return True, full_house
    return False, []

def check_four_of_kind(hand):
    hand_values = [RANKS_MAP.get(card[0]) for card in hand]
    fours = []
    for value in hand_values:
        if hand_values.count(value) == 4 and value not in fours:
            fours.append(value)
    return [True if len(fours) > 0 else False, fours]

def check_straight_flush(hand):
    straight_flushes = []
    suit_value_map = {
        's': [],
        'c': [],
        'h': [],
        'd': [],
    }
    for card in hand:
        suit_value_map.get(card[1]).append(RANKS_MAP.get(card[0]))
        if card[0] == 'A':
            suit_value_map.get(card[1]).append(14)

    for suit in suit_value_map:
        sorted_values = suit_value_map.get(suit)
        sorted_values.sort()
        if len(sorted_values) >= 5:
            for i in range(0, len(sorted_values) - 4):
                if sorted_values[i] == sorted_values[i + 1] - 1 == sorted_values[i + 2] - 2 == sorted_values[i + 3] - 3 == sorted_values[i + 4] - 4:
                    straight_flushes.append(sorted_values[i:i + 5])
    return [True if len(straight_flushes) > 0 else False, straight_flushes]

def check_royal_flush(hand):
    has_straight_flushes, straight_flushes = check_straight_flush(hand)
    royal_flushes = []
    for sf in straight_flushes:
        if sf[0] == 10 and sf[-1] == 14:
            royal_flushes.append(sf)
    return [True if len(royal_flushes) > 0 else False, royal_flushes]