import random

class Card:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value
    
    def present(self):
        return self.__value + " of "+ self.__suit

class Deck(Card):
    
    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.__cards = []
        for i in suits:
            for j in values:
                self.__cards += [Card(i, j)]
        
    def shuffle(self):
        random.shuffle(self.__cards)
    
    def deal(self):
        if len(self.__cards) == 0:
            return None
        else:
            card = self.__cards[-1]
            del self.__cards[-1]
            return card
    
    def count_remaining(self):
        return len(self.__cards)
    
    def get_remaining(self):
        remianing_cards = []
        for i in self.__cards:
            remianing_cards += [i.present()]
        return remianing_cards
