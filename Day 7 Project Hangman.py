import random

words_list = ["keeper", "postman", "coworker", "superman", "animation", "programmer", "code"]
random_word = random.choice(words_list)
split_word = list(random_word)
print(split_word)

for i in range(1,len(split_word)):
    print("_", end="")
print("")

word_input = input("your character guess? ")
word_input_list = []
word_input_list.append(word_input)
print(word_input_list)

while split_word != word_input_list:
    word_input = input("your character guess? ")
    word_input_list.append(word_input)
