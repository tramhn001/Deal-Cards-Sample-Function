import random

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣︎"]
HAND_SIZE = 10

        
def build_deck():
    return[f"{card}{suit}" for card in CARDS for suit in SUITS]

def deal_ten_cards(deck_of_cards):
    dealt_cards = []
    indices_used = set()
    
    while len(dealt_cards) < HAND_SIZE:
        index = random.randint(0, len(deck_of_cards) -1)
        if index not in indices_used:
            dealt_cards.append(deck_of_cards[index])
            indices_used.add(index)
    return dealt_cards

deck = build_deck()
hand = deal_ten_cards(deck)
print("Dealt hand:", hand)