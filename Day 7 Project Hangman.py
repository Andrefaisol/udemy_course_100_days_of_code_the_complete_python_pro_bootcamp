import random

words_list = ["keeper", "kys", "bro", "code", "boob"]
random_word = random.choice(words_list)
split_word = list(random_word)

blank_letters = []
for word in random_word:
    blank_letters.append("_")

print("There a poor man that almost lost his life,"
      "\nif you can guessing the word in 6 times his life will be spared.")
print("Here the word you need to guess:")
for blank in blank_letters:
    print(blank, end="")
print("")
word_input = input("your letter guess? ").lower()
word_input_list = []
word_input_list.append(word_input)

num_letters = 6
urutan = 0

while num_letters != 0:
    for i in random_word:
        if i == word_input:
            blank_letters[urutan] = word_input
            urutan += 1
        else:
            urutan += 1

    num_letters -= 1
    print("Here the word you need to guess:")
    for blank in blank_letters:
        print(blank, end="")
    print("")
    urutan = 0

    if blank_letters == split_word:
        break

    word_input = input("your letter guess? ").lower()

if blank_letters != split_word:
    print("")
    print("You already guess six times and still can't answer")
    print("Poor man lost his live")
    print("The answer is '{}'".format(random_word))
elif blank_letters == split_word:
    print("You saved poor man")
else:
    print("if this printed on console there must be a bug")
