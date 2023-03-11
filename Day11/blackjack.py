import random
import os
from art import logo

print(logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =  random.choice(cards)
    return card

def calculate_score(cards):
   #if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
       return 0 
    
    if 11 in cards and sum(cards) >= 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw 🤣"
    elif computer_score == 0:
        return "Lose, the Opponent has a Blackjack 😥"
    elif user_score == 0:
        return "You Win with a Blackjack"
    elif user_score > 21:
        return "You went over, you Lose!! 😳"
    elif computer_score > 21:
        return "Opponent went over, you Win 😊"
    elif user_score > computer_score:
        return "You Win  🥳"
    else:
        return "You Lose 😔"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your Cards are {user_cards} and sum of cards is {user_score}")
        print(f"Computer's first Card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True 
        else:
            user_should_deal = input(f"Type 'y' to get another card or 'N' to pass ").lower()

            if user_should_deal == 'y': 
                user_cards.append(deal_card())
            else:
                is_game_over = True 

    while computer_score != 0 and computer_score <= 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"In your hand: {user_cards}, final score is {user_score}")
    print(f"In computer's hand: {computer_cards}, final score is {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    os.system('cls')
    play_game()

        







