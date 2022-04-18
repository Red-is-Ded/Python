from art import logo
from art import vs
from replit import clear
from game_data import data
import random 

handle1 = []
handle2 = []

should_continue = 0

# Select random twitter handle, return stats in list.
def pick_twitter():
    twitter1 = random.choice(data)
    twitter1_name = twitter1["name"]
    twitter1_follower_count = twitter1["follower_count"]
    twitter1_description = twitter1["description"]
    twitter1_country = twitter1["country"]

    return [twitter1_name, twitter1_follower_count, twitter1_description, twitter1_country]
    
# compare two twitter users scores. Ask for user guess on comparison. print results and if correct return 0, if incorrect return 1. 
def compare_scores():
    if handle1[2] > handle2[2] and user_guess == "B":
        print(f"That is correct, {handle1[0]} has more followers than {handle2[0]} \n{handle2[0]} has {handle2[1]} followers. Lets try the next question \n \n \n")
        return 0
    elif handle1[2] < handle2[2] and user_guess == "A":
        print(f"That is correct, {handle1[0]} has less followers than {handle2[0]} \n{handle2[0]} has {handle2[1]} followers. Lets try the next question \n \n \n")
        return 0
    else:
        print("I am sorry that is incorrect. You lose.")
        return 1
        
# Introduction. 
print(logo)
print("Welcome to the Higher Lower Game! \n")
print("Guess who has the most twitter followers. \n \n")

# Loop through and display the information from handle1 and handle2, make the comparison and check the users guess, if correct return 0 and if incorrect return 1. 
while should_continue == 0:
    handle1 = pick_twitter()

    print(f"{handle1[0]}, a {handle1[2]} from {handle1[3]}, They have a grand total of {handle1[1]} followers.")

    handle2 = pick_twitter()
    
    print(vs)

    print(f"{handle2[0]}, a {handle2[2]} from {handle2[3]}. Do you think {handle2[0]} has more or less twitter followers? \n \n")

    user_guess = input("Press 'A' for more followers or 'B' for less followers.")

    should_continue = compare_scores()

    clear()
    