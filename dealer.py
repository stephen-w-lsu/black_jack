from deck import Deck
import random

class Dealer():

    def __init__(self):
        self.hand = []
        self.new_deck = Deck()

    def total(self):
        self.total_value = 0
        for card in self.hand:
            self.total_value += card.value
        return self.total_value

    def check_for_ace(self):
        for card in self.hand:
            if card.rank == "Ace":
                card.value = 1
                return True
            else:
                return False

    def shuffle(self):
        random.shuffle(self.new_deck.whole_deck)

    def deal_one_card(self): # Does not work for some reason (dealer.deal_one_card())
        self.new_deck.whole_deck.pop(0) # But works when coded out (deal.new_deck.whole_deck.pop(0)

    def take_one_card(self, dealt_card):
        self.hand.append(dealt_card)
