from typing import List
from src.common.suits_and_ranks import SuitsAndRanks
from src.card import Card
import random

suits_and_ranks = SuitsAndRanks()

suits = suits_and_ranks.get_suits()
ranks = suits_and_ranks.get_ranks()

class Deck:
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' +card.__str__()
        return 'deck has ' + deck_comp


    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_card(self) -> Card:
        single_care = self.deck.pop()
        return single_care

    def split_deck(self):
        half = len(self.deck) // 2
        return self.deck[:half], self.deck[half:]


