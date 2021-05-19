
import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# df = pandas.DataFrame("nato_phonetic_alphabet.csv")


my_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(my_dict)

word = input("Enter a word: ").upper()
result = [my_dict[letter] for letter in word]
print(result)