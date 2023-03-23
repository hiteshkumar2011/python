# Convert the CSV into List in below format
# new_dic {'A': 'Alfa', 'B':'Bravo'}
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
## Loop through rows of data
#{new_key:new_value for (index,row) in df.interrows():

phonetic_dic = {row.letter:row.code for (index,row) in data.iterrows()}
#print(phonetic_dic)

word = input("Enter the word ").upper()
print(word)
# List comphre  #[new_item for item in list]

output_list = [phonetic_dic[char] for char in word]
print(output_list)


