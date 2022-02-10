# Main Game Script
from random import shuffle
from random import choice

# Global Variables
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}
suits=("Hearts","Diamonds","Spades","Clubs")
dealer_names=["Johnny","Harry","Ron","Hermione","Ginny","Stan","Prithvi","Shane"]

# Class Definitions
class Card():

    def __init__(self,suit,rank):
        '''Creates a Card Object and assigns a suit,rank and value from the values dictionary'''
        self.rank=rank
        self.suit=suit
        self.value=values[rank]
        # mask attribute to hide dealer's first card
        self.mask=False
        # is_ace attribute to adjust for aces
        self.is_ace=False
        if self.value==11:
            self.is_ace=True
    
    def __str__(self):
        if self.mask:
            return "Hidden Card"
        else:
            return self.rank +" of "+ self.suit


class Deck():

    def __init__(self):
        '''Creates all 52 cards of a deck and stores it in the DeckList attribute'''
        self.DeckList=[]
        for x in suits:
            for y in values:
                self.DeckList.append(Card(x,y))

    def shuffledeck(self):
        '''Shuffles Decklist using random.shuffle()'''
        shuffle(self.DeckList)
        print("Deck Shuffle Successful.")
    
    def deal_one(self):
        '''Deals and returns one card'''
        return self.DeckList.pop()


class Player():

    def __init__(self,name,bankroll):
        self.name=name
        self.bankroll=bankroll
        self.hand=[]
        self.bet=None
    
    def check_bet(self,bet):
        '''Checks if the bet entered is less than or equal to the Player's bankroll'''
        if bet <= self.bankroll:
            self.bet=bet
            return True
        else:
            return False
    
    def total_value(self):
        '''Returns the total value of the player's hand'''
        tot_value=0
        for x in self.hand:
            tot_value+=x.value
        return tot_value

    def adjust_for_aces(self):
        '''If Player has busted, checks if the hand contains any aces and adjusts them'''
        if self.total_value() >= 21:
            for n in range(len(self.hand)):
                if self.hand[n].is_ace:
                    self.hand[n].value=1
                    # We don't want ALL aces' values to be turned to ones
                    break 
    
    def add_card(self,added_card):
        '''Appends added_card to the Player's hand'''
        self.hand.append(added_card)
        self.adjust_for_aces()
        
    def __str__(self):
        return f"{self.name} has {self.bankroll} amount of money right now."


class Dealer():

    def __init__(self,name=choice(dealer_names)):
        self.name=name
        self.hand=[]

    def total_value(self):
        '''Returns the total value of the dealer's hand'''
        tot_value=0
        for x in self.hand:
            tot_value+=x.value
        return tot_value

    def adjust_for_aces(self):
        '''If Dealer has busted, checks if the hand contains any aces and adjusts them'''
        if self.total_value() >= 21:
            for n in range(len(self.hand)):
                if self.hand[n].is_ace:
                    self.hand[n].value=1
                    # We don't want ALL aces' values to be turned to ones
                    break 
    
    def add_card(self,added_card):
        '''Appends added_card to the Dealer's hand and adjusts for aces.'''
        self.hand.append(added_card)
        self.adjust_for_aces()
    
    def final_display_cards(self):
        '''Function to display cards at the end of each round and to remove the mask on the first card of the dealer's hand'''
        print(f"Dealer, {dealer.name}'s cards:")
        self.hand[0].mask=False
        for x in dealer.hand:
            print(x)

# Functions Definitions
def check_bust(n,hand=[]):
    '''Parameter as hand, checks if player or dealer has busted (cards have more value than n)'''
    total_value=0
    for x in hand:
        total_value+=x.value
    if total_value>n:
        return True     # Busted!
    else:
        return False    # No Bust.
    
# Game Start

game_on=True

while game_on:

    # Creating and shuffling the deck
    
    deck=Deck()
    deck.shuffledeck()

    # Setting up the player and the dealer (computer player)
    while True:
        try:
            player1=Player(name=input("Enter your name:"),bankroll=float(input("Enter your bankroll (money given):")))
            break    
        except:
            print("An Error Occurred, Please try again.")
    
    dealer=Dealer()

    while True:
        

        # Asking Player for bet
        while True:
            try:
                if player1.check_bet(float(input(f"{player1.name}, currently have: \n {player1.bankroll} in your bankroll \n Enter your bet, {player1.name}:"))):
                    print("Bet Valid.")
                    break
                else:
                    print("Invalid Bet, Insufficient Funds. Please Try Again.")
                    continue
            except:
                print("An Error Occurred, Please Try Again.")

        # Dealing Cards

        for x in range(2):
            player1.add_card(deck.deal_one())
            dealer.add_card(deck.deal_one())

        # Displaying the Cards

        print(f"Dealer, {dealer.name}'s cards:")
        dealer.hand[0].mask=True
        for x in dealer.hand:
            print(x)
        print(f"Player, {player1.name}'s cards:")
        for x in player1.hand:
            print(x)

        # Asking player if they would like to hit/stand
        while player1.total_value()<=21:
            hitchoice=None
            while hitchoice not in ['H','S']:
                try:
                    hitchoice=input("Would you like to hit or stand?(H/S):")
                except:
                    print("Invalid Input, Please Try Again.")
                    hitchoice=None
            if hitchoice=='H':
                player1.add_card(deck.deal_one())
                print(f"Player, {player1.name}'s cards:")
                for x in player1.hand:
                    print(x)
            else:
                break
        else:
            print(f"Player, {player1.name} Busted!")
            print(f"Dealer {dealer.name} wins!")
            print(f"Dealer, {dealer.name}'s cards:")
            dealer.hand[0].mask=False
            for x in dealer.hand:
                print(x)
            player1.bankroll-=player1.bet
            print(f"Player, {player1.name}'s bet of $ {player1.bet} has been lost.")
            print(f"Player, {player1.name} now has $ {player1.bankroll} left")
            game_on_choice=None
            while game_on_choice not in ['Y','N']:
                try:
                    game_on_choice=input("Would you like to play again?(Y/N):")
                except:
                    print("Invalid Input, Please Try Again.")
                    game_on_choice=None
            if game_on_choice:
                game_on=True
                break
            else:
                game_on=False
                break

        # Dealer hits until their value ¬meets or¬ exceeds 17
        while dealer.total_value()<=17:
            dealer.add_card(deck.deal_one())
        print(f"Dealer, {dealer.name}'s cards:")
        for x in dealer.hand:
            print(x)
        
        # Figuring out who has won

        # Displaying everyone's total value:
        print(f"Player, {player1.name}'s total value: {player1.total_value()}")
        print(f"Dealer, {dealer.name}'s total value: {dealer.total_value()}")

        # Checking if anyone has busted/ who has won
        both_bust=check_bust(21,player1.hand) and check_bust(21,dealer.hand) # Boolean condition variable to check if both dealer
        both_not_bust= (not check_bust(21,player1.hand)) and (not check_bust(21,dealer.hand))
        
        if both_bust or both_not_bust:
            if player1.total_value()>dealer.total_value():
                dealer.final_display_cards()
                print(f"Player {player1.name} wins!")
                player1.bankroll+=player1.bet
                print(f"Player, {player1.name}'s bet of $ {player1.bet} has been won!")
                print(f"Player, {player1.name} now has $ {player1.bankroll} left")
                while True:
                    try:
                        choice=input("Would you like to play again?(Y/N)")
                        if choice.upper()=='Y':
                            game_on=True
                            break
                        elif choice.upper()=='N':
                            game_on=False
                            print("Thanks for playing! Goodbye!")
                            break
                    except:
                        print("Incorrect Input, Please Try Again.")
                break
            elif player1.total_value()<dealer.total_value():
                dealer.final_display_cards()
                print(f"Dealer {dealer.name} wins!")
                player1.bankroll-=player1.bet
                print(f"Player, {player1.name}'s bet of $ {player1.bet} has been lost.")
                print(f"Player, {player1.name} now has $ {player1.bankroll} left")
                while True:
                    try:
                        choice=input("Would you like to play again?(Y/N)")
                        if choice.upper()=='Y':
                            game_on=True
                            break
                        elif choice.upper()=='N':
                            game_on=False
                            print("Thanks for playing! Goodbye!")
                            break
                    except:
                        print("Incorrect Input, Please Try Again.")
                break
            else:
                print("Tie!")
                while True:
                    try:
                        choice=input("Would you like to play again?(Y/N)")
                        if choice.upper()=='Y':
                            game_on=True
                            break
                        elif choice.upper()=='N':
                            game_on=False
                            print("Thanks for playing! Goodbye!")
                            break
                    except:
                        print("Incorrect Input, Please Try Again.")
                break
        elif check_bust(21,player1.hand):
            dealer.final_display_cards()
            print(f"{player1.name} busted!")
            print(f"Dealer {dealer.name} wins!")
            player1.bankroll-=player1.bet
            print(f"Player, {player1.name}'s bet of $ {player1.bet} has been lost.")
            print(f"Player, {player1.name} now has $ {player1.bankroll} left")
            while True:
                try:
                    choice=input("Would you like to play again?(Y/N)")
                    if choice.upper()=='Y':
                        game_on=True
                        break
                    elif choice.upper()=='N':
                        game_on=False
                        print("Thanks for playing! Goodbye!")
                        break
                except:
                    print("Incorrect Input, Please Try Again.")
            break
        elif check_bust(21,dealer.hand):
            dealer.final_display_cards()
            print(f"{dealer.name} busted!")
            print(f"Player {player1.name} wins!")
            player1.bankroll+=player1.bet
            print(f"Player, {player1.name}'s bet of $ {player1.bet} has been won!")
            print(f"Player, {player1.name} now has $ {player1.bankroll} left")
            while True:
                try:
                    choice=input("Would you like to play again?(Y/N)")
                    if choice.upper()=='Y':
                        game_on=True
                        break
                    elif choice.upper()=='N':
                        game_on=False
                        print("Thanks for playing! Goodbye!")
                        break
                except:
                    print("Incorrect Input, Please Try Again.")
            break

# Game End



        

    
