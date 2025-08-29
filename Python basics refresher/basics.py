import random

#Create a rock-paper-scissors game
def get_choices():
    player_input = input("Choose among these three: Rock, Paper, Scissors.")
    computer_input = "Program unfinished. Functionality incomplete."
    choices = {"player_choice ": player_input, "computer_choice": computer_input}
    return choices

#Example function

def greeting():
    return "Surprise mf."

response_1 = greeting()

choices = get_choices()

#print(response_1)
#print(choices)
#print("Hello world")
#dictionaries

dict1 = {"name": "Boy", "color": "Chicken feather brown"}

#Lists

this_is_a_list = [1, 2, 23, 4, 55, 6, 17, 8888, "09", "Food like chicken", "Food Like BEEF"]

list_item = random.choice(this_is_a_list)

#F-string

color = "Baby vomit yellow"
car = "Toyota GR Yaris"

print(f"The {car} comes in various color options, including but not limited to {color}")

