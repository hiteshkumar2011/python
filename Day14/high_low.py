import random
import os
from game_data import data
from art import logo,vs
# Display art

def format_data(account):
    """
Format the account data into printable format 
    """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name} a {account_desc} from {account_country}")

def check_answer(guess,a_followers,b_followers):
    """
    Check if user is correct
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
print(logo)

# Generate random account from game data
account_b = random.choice(data)
score = 0
should_continue = True


# Make game repeatable 
while should_continue:
    # Making the account at position B become next account at position A 
    account_a = account_b
    account_b = random.choice(data)
    while  account_a == account_b:
        account_b = random.choice(data)

    # Format the account data into printable format 
    print(f"Compare Account A: {format_data(account_a)}. ")
    print(vs)
    print(f"Compare Account B: {format_data(account_b)}. ")

    # Ask user for a guess 
    guess = input("Who has more followers ? Type A or B : ").lower()
    
    # Clear the screen after each rounds
    os.system('cls')
    print(logo)
    # Check if user is correct
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_answer(guess,a_followers,b_followers)

    # Give user feedback & Score Keeping

    if is_correct:
        score +=1
        print(f"You are right !! Your Current score: {score} ")
        
    else:
        should_continue = False 
        print(f"Sorry, That's wrong. Final Score: {score} ")


