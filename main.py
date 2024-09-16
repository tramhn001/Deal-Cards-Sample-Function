import random

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣︎"]
HAND_SIZE = 10

def build_deck():
    return [f"{card}{suit}" for card in CARDS for suit in SUITS]

# write a function that deals 10 cards from a deck of cards without using the sample function
def deal_ten_cards(deck_of_cards):
    pass