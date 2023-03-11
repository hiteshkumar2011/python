from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt (plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text,shift_amount):
    decrypt_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decrypt_text += new_letter
    print(f"The decoded text is {decrypt_text}")

######CUT DOWN THE CODE USING CAESAR FUNCTION #########
def caesar(start_text,shift_amount,cipher_direction):
    endtext=""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            endtext += alphabet[new_position]
        else:
            endtext +=char
    print (f" The {cipher_direction}d value of {start_text} is {endtext}")
    
should_continue = False
while not should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26        
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    result = input(f"Do you want to continue,Type 'Yes' or 'No'").lower()
    if result == "no":
        should_continue = True  
        print("GoodBye")
