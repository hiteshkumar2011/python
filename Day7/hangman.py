import random
import os
from hangman_art import stages, logo
from hangman_words import word_list
print(logo)
#word_list = ["aardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
#print(chosen_word)
lives = 6
display = []
for letter in chosen_word:
    display +="_"
print(display)

end_of_game = False
while  not end_of_game:
    guess = input("Guess the letter: ").lower()  ### Ask User to Choose the letter
    os.system('cls')
    if guess in display:
        print(f"You already guessed this letter")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        lives -=1
        print(f"You guessed a letter {guess} ,which is not in the word, You loose a Life!!")
        if lives ==0:
            end_of_game = True
            print("You Loose")
    print(stages[lives])
    
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game = True 
        print("You Win")
    

            





