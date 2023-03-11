# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
 
# Function to check the user answer
def check_answer(guess,answer,turns):
    """
    checks answer against the guess return the number of turns remaining 
    """
    if guess > answer:
        print ("Too High")
        return turns -1
    elif guess < answer:
        print ("Too Low")
        return turns -1
    else:
        print(f"You got it right. The answer was {answer}")

def set_diffculty():
        level = input ("Choose the Difficulty. Type 'Easy' or 'Hard' ").lower()
        if level == 'easy':
             return EASY_LEVEL_TURN
        else:
             return HARD_LEVEL_TURN
        
def game():
    # Include an ASCII art logo.
    print (logo)
    print("Welcome to Number Guessing Game !! ")
    # Allow the player to submit a guess for a number between 1 and 100.
    print("I'm thinking of a number between 1 to 100 ")
    answer = random.randint(1,100)
    print(f"The correct answer is {answer}")
    turns = set_diffculty()
    guess = 0
    while guess != answer:  
        print(f"You have {turns} attempts remaining to guess the number")   
        guess = int(input("Make a guess!! "))
        turns = check_answer (guess,answer,turns)
        if turns == 0:
            print (f"You have run out of guesses, you lose !!")
            return 
        elif guess !=answer:
             print(f"Guess Again ") 
game()



