import time
from dealer import Dealer
from player import Player

player = Player()
dealer = Dealer()
dealer.shuffle()

# Deal player and dealer 2 cards each
for _ in range(2):
    player.take_one_card(dealer.new_deck.whole_deck.pop(0))
    dealer.take_one_card(dealer.new_deck.whole_deck.pop(0))
time.sleep(0.5)
print(f"Welcome to my Blackjack Table!")
game_on = True
while game_on:
    player_turn = True
    dealer_turn = False

    time.sleep(1)
    print(f"Your current chip count is {player.bankroll}")
    time.sleep(1)
    if player.bankroll <= 0:
        print("Sorry. You are out of chips.")
        time.sleep(1)
        player_turn = False
        game_on = False

    # Take bet and check if bankroll covers bet
    bet = 100000
    while bet > player.bankroll:
        bet = int(input("Please place your bet: "))
        time.sleep(1)
        if bet > player.bankroll:
            print("Insufficient Funds!")
            time.sleep(1)
        else:
            bet = bet

    print(f"You have {player.hand[0]}")
    time.sleep(1)
    print(f"and {player.hand[1]}")
    time.sleep(1)
    print(f"Total is {player.total()}.")
    time.sleep(1)
    print(f"Dealer shows {dealer.hand[0]}.")
    time.sleep(1)
    print(f"Total of {dealer.hand[0].value}")
    time.sleep(1)

    # Check for Blackjacks
    # Both player and dealer Blackjacks
    if player.total() == 21 and dealer.total() == 21:
        print("Both you and dealer have Blackjack. Push.")
        time.sleep(1)
        player.push()
        player_turn = False
        game_on = False

    # Player Blackjack
    elif player.total() == 21:
        print("You have Blackjack!")
        time.sleep(1)
        player.win_black_jack(bet)
        player_turn = False
        game_on = False

    # Dealer Blackjack
    elif dealer.total() == 21:
        print("Dealer has Blackjack")
        time.sleep(1)
        player.lost_bet(bet)
        player_turn = False
        game_on = False

    # No Blackjack, continue game play
    while player_turn:
        # Player hit or stay conditions
        player_choice = input("Hit or Stay:(H/S) ")
        time.sleep(1)
        if player_choice.upper() == "H":
            new_card = dealer.new_deck.whole_deck.pop(0)
            print(f"You draw {new_card}")
            player.take_one_card(new_card)
            time.sleep(1)
            print(f"Total is {player.total()}")
            time.sleep(1)
            # Check for Ace
            if player.total() > 21:
                if not player.check_for_ace():
                    print("Player Bust.")
                    time.sleep(1)
                    print(f"Dealer has {dealer.hand[0]} and {dealer.hand[1]}. Total is {dealer.total()}")
                    time.sleep(1)
                    player.lost_bet(bet)
                    time.sleep(1)
                    player_turn = False
                    dealer_turn = False
                    game_on = False
                else:
                    continue
        if player.total() == 21:
            print("Player has 21.")
            time.sleep(1)
            player_turn = False
            dealer_turn = True
        if player_choice.upper() == "S":
            player_turn = False
            dealer_turn = True

    while dealer_turn:
        print(f"Dealer has {dealer.hand[0]} and {dealer.hand[1]}. Total is {dealer.total()}")
        time.sleep(1)
        # Draw card until soft 17
        while dealer.total() < 17:
            dealer_new_card = dealer.new_deck.whole_deck.pop(0)
            print(f"Dealer draws {dealer_new_card}")
            time.sleep(1)
            dealer.take_one_card(dealer_new_card)
            print(f"Dealer has {dealer.total()}")
            time.sleep(1)

        if dealer.total() > 21:
            if not dealer.check_for_ace():
                print("Dealer Bust.")
                time.sleep(1)
                player.win_bet(bet)
                time.sleep(1)
                dealer_turn = False
                game_on = False
            else:
                continue

        elif dealer.total() == player.total():
            print("Push.")
            time.sleep(1)
            player.push()
            time.sleep(1)
            dealer_turn = False
            game_on = False

        elif dealer.total() > player.total():
            print("Dealer Won.")
            time.sleep(1)
            player.lost_bet(bet)
            time.sleep(1)
            dealer_turn = False
            game_on = False

        else:
            print("Player Won.")
            time.sleep(1)
            player.win_bet(bet)
            time.sleep(1)
            dealer_turn = False
            game_on = False

    # Ask if player wants to reload
    if player.bankroll <= 0:
        reload = input("Would you like to reload you chips? Y/N ")
        if reload.upper() == "Y":
            player.bankroll = 1000
        else:
            print(f"Thank you for playing! You left the table with {player.bankroll} chips.")
            game_on = False
            break

    # Ask if player wants to continue
    wrong_input = True
    while wrong_input:
        keep_playing = input("Keep Player? Y/N ")
        if keep_playing[0].upper() == "Y":
            wrong_input = False
            player.hand.clear()
            dealer.hand.clear()
            for _ in range(2):
                player.take_one_card(dealer.new_deck.whole_deck.pop(0))
                dealer.take_one_card(dealer.new_deck.whole_deck.pop(0))
            player_turn = True
            game_on = True
        elif keep_playing[0].upper() == "N":
            wrong_input = False
            time.sleep(1)
            print(f"Thank you for playing! You left the table with {player.bankroll} chips.")
        else:
            print("Sorry. I did not understand you. Please enter again.")
