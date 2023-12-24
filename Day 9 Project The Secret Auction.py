import os
import string


bidders = {}
auction = True
while auction:
    # input bidder name
    name = string.capwords(input("What is your name?: ").lower())

    # make bid only number
    bid = input("How many you gonna bid?: $")
    while not bid.isdigit():
        bid = input("How many you gonna bid?: $")
    bid_int = int(bid)

    # adding input to bidders dictionary
    bidders[name] = bid_int

    # if any new bidder clean console and looping, if not break loop
    new_entry = input("Any other bidders? Type 'yes' or 'no'\n").lower()
    while new_entry != "yes" and new_entry != "no":
        new_entry = input("Any other bidders? Type 'yes' or 'no'\n").lower()
    if new_entry != "yes":
        auction = False
    else:
        os.system("cls")

# winner bidder selection
indicator = 0
bidders_winner = ""
bid_value = ""
for bid in bidders:
    if indicator < bidders[bid]:
        indicator = bidders[bid]
        bidders_winner = bid
        bid_value = bidders[bid]

# print the winner and the amount bid
print(f"The winner is {bidders_winner} with bid ${bid_value}")
