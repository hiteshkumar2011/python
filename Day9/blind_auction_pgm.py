from art import logo
import os
print (logo)
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid =0
    winner = ""
    for bidder in bidding_record:
        if (bidding_record[bidder]) > highest_bid :
            highest_bid = bidding_record[bidder]
            winner = bidder 
    print(f"The highest bidder is {winner} with a value of {highest_bid}")


while not bidding_finished:
    name = input("What is your name? ")
    bid_price = int(input("What is your bid? $ "))
    bids[name] = bid_price
    should_continue = input("Do we have any other user, Type 'Yes' or 'No' ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')


    

