import blackjack_deck
import blackjack_card

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
    
    def add_card(self, card_list):
        self.cards.extend(card_list)
        
    def value_calculator(self):
        self.value = 0
        has_ace = False
        
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
                
        if has_ace and self.value > 21:
            self.value -= 10
            
    def peek_value(self):
        self.value_calculator()
        return self.value
    
    def is_blackjack(self):
        return self.peek_value() == 21
    
    def peek_at_hand(self, show_all_dealer_cards=False):
        print(f''' {"Dealer's" if self.dealer else "Your"} hand: ''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer\
                and not show_all_dealer_cards\
                    and not self.is_blackjack():
                print("Hidden")
            else:
                print (card)
        
        if not self.dealer:
            print("Value:", self.peek_value())
        print()

deck = blackjack_deck.Deck()
