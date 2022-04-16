import random
from logo import logo

print(logo)

# Intro and user to select difficulty
print("Welcome to the guessing game! \n")
print("I´m thinking of a number between 1 and 100, can you guess what that number is? \n")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")


#select a random number
random_number = random.randint(1, 100)
# for troubleshooting uncomment below:
#print(random_number)

game_cont = True 

# set number of goes depending on difficulty
if difficulty == "easy":
    print("You have 10 guesses.")
    guess_num = 10
else:
    print("You have 5 guesses.")
    guess_num = 5

# take users guess, loop through and apply game logic, remove one guess per go, and set game to stop on win or all lives lost. 
while game_cont:
    guess_num -= 1
    print(f"You have {guess_num + 1} guesses remaining")
    guess = int(input("make your guess: \n"))
    if guess_num == 0:
        game_cont = False
        print("out of guesses, you lose.")
    elif guess > random_number:
        print("Too High!")
    elif guess < random_number:
        print("Too Low!")
    else:
        print(f"You are correct, the number was {random_number}")
        game_cont = False


    