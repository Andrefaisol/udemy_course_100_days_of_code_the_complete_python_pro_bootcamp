import random

words_list = ["keeper", "kys", "bro", "code", "boob"]
random_word = random.choice(words_list)
split_word = list(random_word)

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
hangman_lives = 0

blank_letters = []
for word in random_word:
    blank_letters.append("_")

print("There a poor man that almost lost his life,"
      "\nif you can guessing a letter in the word less than 6 wrong answer\n"
      "then his life will be spared.")
print("Here the word you need to guess:")
for blank in blank_letters:
    print(blank, end="")
print("")
print(hangman[hangman_lives])

num_letters = 6
urutan = 0

while num_letters != 0:

    word_input = input("your letter guess? ").lower()

    while len(word_input) != 1:
        print("please input only a letter")
        word_input = input("your letter guess? ").lower()

    for i in random_word:
        if i == word_input:
            blank_letters[urutan] = word_input
            urutan += 1
        else:
            urutan += 1

    if word_input not in blank_letters:
        num_letters -= 1
        hangman_lives += 1

    print("Your guessing letter is '{}'".format(word_input))
    print("You still have {} chance".format(num_letters))
    print(hangman[hangman_lives])

    if blank_letters == split_word:
        break

    print("Here the word you need to guess:")

    for blank in blank_letters:
        print(blank, end="")

    print("")
    urutan = 0

if blank_letters != split_word:
    print("")
    print("You already wrong six times and still can't answer")
    print(hangman[6])
    print("Poor man lost his live")
    print("The answer is '{}'".format(random_word))
elif blank_letters == split_word:
    print("You saved the poor man")
else:
    print("if this printed on console there must be a bug")


