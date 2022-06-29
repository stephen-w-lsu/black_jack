STARTING_BANKROLL = 1000

class Player():

    def __init__(self):
        self.hand = []
        self.bankroll = STARTING_BANKROLL

    def take_one_card(self, dealt_card):
        self.hand.append(dealt_card)

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

    def win_black_jack(self, bet):
        self.bankroll += (bet * 1.5)
        print(f"You won! Your chip count is {self.bankroll}")

    def lost_bet(self, bet):
        self.bankroll -= bet
        print(f"Dealer won! Your chip count is {self.bankroll}")

    def win_bet(self, bet):
        self.bankroll += bet
        print(f"You won! Your chip count is {self.bankroll}")

    def push(self):
        self.bankroll = self.bankroll
        print(f"Your chip count is {self.bankroll}")