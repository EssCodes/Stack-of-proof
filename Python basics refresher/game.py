#A rock-paper-scissors game

import random

def get_choices():
    player_choice = input("Enter a choice: Rock; Paper; Scissors: ")
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    choices = {"Player": player_choice, "Computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose: {player}; The computer 'chose': {computer}")
    
    #First version
    #if player == computer:
    #    print("None of y'all won tho.")
    #elif player == "Rock" and computer == "Paper":
    #    print("Aight bro you lost.")
    #elif player == "Rock" and computer == "Scissors":
    #    print("Aight 'Rocky' you won this.")
    #elif player == "Paper" and computer == "Rock":
    #    print("Aight unc you won this.")
    #elif player == "Paper" and computer == "Scissors":
    #   print("Damn unc looks like you got cut in two.")
    #elif player == "Scissors" and computer == "Rock":
    #    print("Unc got bouldered.")
    #else:
    #    print("Look at bro all happy he won one. Finna get the ground swept up from under ya.")
    
    #Second version
    
    if player == computer:
        print("None of y'all won tho.")
    elif player == "Rock":
        if computer == "Paper":
            print("Aight bro you lost.")
        else:
            print("Aight 'Rocky' you won this.")
    elif player == "Paper":
        if computer == "Rock":
            print("Aight unc, you got me.")
        else:
            print("Damn unc, you got cut in two.")
    elif player == "Scissors":
        if computer == "Rock":
            print("Unc got smashed like the hulk on scene")
        else:
            print("Look at bro all happy he won one. Finna get the ground swept up from under ya.")
    else:
        print("Sorry bruv, the game broke....")
          
choices = get_choices()

result = check_win(choices["Player"], choices["Computer"])

print(result)