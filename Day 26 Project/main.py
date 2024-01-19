import pandas


# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {b.letter: b.code for (a, b) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
words = " "
while not words.isalpha():
    words = input("Enter Your word you want to code: ").upper()
word_list = [alpha for alpha in words]
code_list = [new_dict[i] for i in word_list]
print(code_list)

