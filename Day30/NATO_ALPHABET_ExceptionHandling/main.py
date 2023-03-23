# Convert the CSV into List in below format
# new_dic {'A': 'Alfa', 'B':'Bravo'}
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dic)

def generate_phonetic():
    word = input("Enter the word ").upper()
    try:
        output_list = [phonetic_dic[letter] for letter in word]
    except:
        print("Sorry, Only letters in the Alphabet please. ")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()


