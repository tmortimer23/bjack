from random import shuffle

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

values = {'2': 2, '3': 3, '4': 4, '5': 5,
          '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
          }

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def show(self):
        print(self.rank + " of " + self.suit)
        
class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for i in suits:
            for j in ranks:
                self.cards.append(Card(i, j))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self, num):
        for i in range(num):
            shuffle(self.cards)

class Player():
    def __init__(self):
        self.bank_roll = 0
        self.hand = []

    def show_card(self):
        self.hand[1].show()

    def show_hand(self):
        for card in self.hand:
            card.show()

    def show_bank_roll(self):
        print("Your current bank roll is $" + str(self.bank_roll) + ".")

    def wager(self):
        bet = int(input("How much would you like to wager? "))
        if bet >= 10 and bet <= self.bank_roll:
            self.bank_roll -= bet
            print("You've just wagered $" + str(bet) + ".\n")

    def total(self):
        total = 0
        
        for card in self.hand:
            if card.rank != 'A':
                value = values[card.rank]
                total += value
            else:
                if total >= 11:
                    value = 1
                    total += value
                else:
                    value = 11
                    total += value

        print(total)
        return total                   
            
    def reorder(self):
        for card in self.hand:
            if card == 'A':
                self.hand.append(self.hand.pop(self.hand.index('A')))

    def hit_or_stay(self, deck):
        x = False
        while x != True:
            prompt = "\nHit or Stay? "
            choice = input(prompt)
            if choice == 'hit':
                self.hand.append(deck.cards.pop())
                self.reorder()
                self.show_hand()
                self.total()
                if self.total() > 21:
                    x = True
                    print("Sorry, looks like you busted!")
                else:
                    continue
            elif choice == 'stay':
                x = True

            else:
                print("please enter a valid response")

    
