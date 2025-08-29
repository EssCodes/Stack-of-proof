import random
import blackjack_card

class Deck:
    def __init__(self):
        self.cards = []
        
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "Ace", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "Jack", "value": 10},
            {"rank": "Queen", "value": 10},
            {"rank": "King", "value": 10}
        ]
        for suit in suits:
            for rank in ranks:
                card = blackjack_card.Card(suit, rank)
                self.cards.append(card)
        if len(self.cards) == 52:
            print("Deck ready.")
                       
    def shuffle_deck(self):
        random.shuffle(self.cards)
   
        
    def card_dealing(self, number):
       cards_dealt = []
       counter = 0
       while counter < number:
        cards_dealt.append(self.cards.pop())
        counter += 1
       return cards_dealt
        
            