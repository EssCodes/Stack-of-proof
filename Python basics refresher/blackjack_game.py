import blackjack_deck
import blackjack_hand

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0
        
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play?"))
            except:
                print("Sorry bruv that's not a number, innit?")
        
        while game_number < games_to_play:
            game_number += 1
            
            deck = blackjack_deck.Deck()
            deck.shuffle_deck()
            
            hand = blackjack_hand.Hand()
            dealer_hand = blackjack_hand.Hand(dealer=True)
            for i in range(2):
                hand.add_card(deck.card_dealing(1))
                dealer_hand.add_card(deck.card_dealing(1))
            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}.")
            print("*" * 30)
            hand.peek_at_hand()
            dealer_hand.peek_at_hand()
            
            if self.check_for_win(hand, dealer_hand):
                continue
            
            choice = "" 
            
            while hand.peek_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Wanna hit or stand? (h/s) ").lower()
                print()
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Nah bruv. 'Hit' OR 'Stand' (also accepted: H/S)").lower()
                    print()
                if choice in ["hit", "h"]:
                   hand.add_card(deck.card_dealing(1))
                   hand.peek_at_hand()
                   
            if self.check_for_win(hand, dealer_hand):
                continue
            
            hand_value = hand.peek_value()
            dealer_hand_value = dealer_hand.peek_value()
            
            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.card_dealing(1))
                dealer_hand_value = dealer_hand.peek_value()
                
            dealer_hand.peek_at_hand(show_all_dealer_cards=True)
            if self.check_for_win(hand, dealer_hand):
                continue
            
            print(f"The Jig is up. You had {hand_value} while the dealer had {dealer_hand_value}")
            
            self.check_for_win(hand, dealer_hand, True)
        try:
            again = input("The game is over. Wanna play again? (y/n)").lower()
            if again in ["y", "yes"]:
                self.play()
            else:
                print("Alright then, catch you later, innit?")
        except:
            print("\nThanks for playing bruv.")
            
    
    def check_for_win(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.peek_value() > 21:
                print("Bruv, you busted. The dealer won this.")
                return True
            elif dealer_hand.peek_value() > 21:
                print("Dealer busted bruv. This one is in your bag.")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Its a draw bruv, calm it.")
                return True
            elif player_hand.is_blackjack():
                print("He ain't got nothing on you. You won bruv.")
                return True
            elif dealer_hand.is_blackjack():
                print("You lost this one. Up for another round?")
                return True
        else:
            if player_hand.peek_value() > dealer_hand.peek_value():
                print("Nice one. He didn't see it coming.")
            elif player_hand.peek_value() == dealer_hand.peek_value():
                print("Tied.")
            else:
                print("Dealer got this one. Go take a rest bruv.")
            return True
        return False   
            