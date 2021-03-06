from replit import clear
from art import logo

print(logo)

print("Welcome to the secret auction program.")

go_again = True


bids = {}
def bid_collection(name, bid):
    bids[bid] = name

while go_again == True:
    bid_counter = 0
    bidder_name = input("What is your name? \n")
    highest_bid = input("What is your highest bid? \n")
    bid_collection(bidder_name, highest_bid)
    cont = input("Are there any more bids? Type yes or no. \n")
    if cont == "yes":
        clear()
    else:
        winner = max(bids)
        winner_name = bids[winner]
        print(f"the Winner is {winner_name} and the winning bid is {winner}.")
        print("Thank you for playing.")
        go_again = False