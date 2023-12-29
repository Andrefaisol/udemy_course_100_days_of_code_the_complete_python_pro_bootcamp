import random

CHOSE_NUMBER = random.randint(1, 100)
EASY = 10
HARD = 5


def input_level():
    level = input("Choose what level do you want to play, type 'easy' or 'hard': ").lower()
    while level != "easy" and input_level != "hard":
        level = input("Choose what level do you want to play, type 'easy' or 'hard': ").lower()
    return level

def level_check(level):
    global EASY
    global HARD
    count = 0
    if level == "easy":
        count += EASY
    else:
        count += HARD
    return count


def guessing():
    number_guess = input("Type your number guess here: ")
    while not number_guess.isdigit() or (int(number_guess) < 1 or int(number_guess) > 100):
        number_guess = input("Type your number guess here: ")
    answer[0] = int(number_guess)


def is_it_right(number):
    global CHOSE_NUMBER
    if number < CHOSE_NUMBER:
        print("too low")
    elif number > CHOSE_NUMBER:
        print("too high")


answer = [0]
game = True
while game:

    many_guess = level_check(input_level())

    while answer[0] != CHOSE_NUMBER:
        if many_guess == 0:
            print("You run out of guess attempt")
            break
        guessing()
        is_it_right(answer[0])
        many_guess -= 1
        print(f"You have {many_guess} more attempt to guess")
    print("==========================")
    print("Your guess number is right")
