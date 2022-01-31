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
    
    def __str__(self):
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
    
    def check_bet(self,bet):
        '''Checks if the bet entered is less than or equal to the Player's bankroll'''
        if bet <= self.bankroll:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.name} has {self.bankroll} amount of money right now."


class Dealer():

    def __init__(self,name=choice(dealer_names)):
        self.name=name
        self.hand=[]


# Functions Definitions
def check_bust(hand=[]):
    '''Parameter as hand, checks if player or dealer has busted (cards have more value than 21)'''
    total_value=0
    for x in hand:
        total_value+=x.value
    if total_value>21:
        return True     # Busted!
    else:
        return False    # No Bust.
    


    
