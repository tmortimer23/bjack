import blackjack

def main():
    active = True
    while active:
        user_response = input("Would you like to play a game of blackjack? (y/n) ")
        if user_response == 'y':
            print("Game beginning\n")
            initiate_game()
            break
        elif user_response == 'n':
            print("Come back later...")
            break
        else:
           print("Please enter a valid response")

def initiate_game():
    dealer = blackjack.Player()
    
    player1 = blackjack.Player()
    player1.bank_roll = 500
    
    deck = blackjack.Deck()
    deck.shuffle(5)

    player1.show_bank_roll()
    player1.wager()

    for i in range(2):
        player1.hand.append(deck.cards.pop())
        dealer.hand.append(deck.cards.pop())

    player1.reorder()
    dealer.reorder()

    print("You were dealt...")
    player1.show_hand()
    player1.total()

    print("\nThe dealer is showing...")
    dealer.show_card()

    player1.hit_or_stay(deck)

    

        

main()
