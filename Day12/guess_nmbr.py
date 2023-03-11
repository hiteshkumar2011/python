import random
from art import logo
EASY_LEVEL_COUNTER = 5
HARD_LEVEL_COUNTER = 10

def check_number(guess,answer,turns):
    if guess > answer:
        print("Too High")
        return turns -1
    elif guess < answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You got the right answer, the answer is {answer}")

def set_difficulty():
    level = input ("Choose the Difficulty. Type 'Easy' or 'Hard' ").lower()
    if level == 'easy':
        return EASY_LEVEL_COUNTER
    else:
        return HARD_LEVEL_COUNTER

def game():
    print (logo)
    print("Welcome to Number Guessing Game !! ")
    # Allow the player to submit a guess for a number between 1 and 100.
    print("I'm thinking of a number between 1 to 100 ")
    answer = random.randint(1,100)
    print(f"The correct answer is {answer}")
    turns = set_difficulty() 
    guess =0 
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess!! "))
        turns = check_number(guess,answer,turns)
        if turns == 0:
            print (f"You have run out of guesses, you lose !!")
            return 
        elif guess !=answer:
             print(f"Guess Again ")

game()


         

