from random import randint
import os

library = [
    {"name": "Whatsapp",
     "downloaded": "9.66", },
    {"name": "Facebook",
     "downloaded": "7.57", },
    {"name": "Messenger",
     "downloaded": "5.61", },
    {"name": "TikTok",
     "downloaded": "4.51", },
    {"name": "Instagram",
     "downloaded": "4.14", },
    {"name": "Facebook Lite",
     "downloaded": "2.92", },
    {"name": "SHAREit",
     "downloaded": "2.21", },
    {"name": "Netflix",
     "downloaded": "1.88", },
    {"name": "Snapchat",
     "downloaded": "1.71", },
    {"name": "Telegram",
     "downloaded": "1.63", },
    {"name": "Subway Surfers",
     "downloaded": "1.57", },
    {"name": "Spotify",
     "downloaded": "1.41", },
    {"name": "Free Fire",
     "downloaded": "1.39", },
    {"name": "X",
     "downloaded": "1.38", },
    {"name": "Candy Crush Saga",
     "downloaded": "1.32", },
    {"name": "Skype",
     "downloaded": "1.17", },
    {"name": "MX Player",
     "downloaded": "1.16", },
    {"name": "Viber",
     "downloaded": "1.10", },
    {"name": "My Talking Tom",
     "downloaded": "1.03", },
    {"name": "UC Browser",
     "downloaded": "1.00", },
    ]


def random_number():
    random = randint(0, 19)
    return random


game = True
while game:

    print("Welcome to Higher Lower game, You will compare and guess which media social that most downloaded.")
    print("The game will stop once your guess is wrong.")
    print("====================================================================")
    correct = 0
    question = True
    while question:
        index1 = 0
        index2 = 0
        while index1 == index2:
            index1 = random_number()
            index2 = random_number()

        answer = ""
        while answer != "higher" and answer != "lower":
            answer = input(f"Does {library[index1]["name"]} is higher or lower compared with {library[index2]["name"]}?"
                           f"\n(Type 'higher' or 'lower'): ").lower()

        compare = library[index1]["downloaded"]
        compared = library[index2]["downloaded"]

        parameter = 2
        if compare > compared:
            parameter = 1
        elif compare < compared:
            parameter = 0

        if parameter == 1 and answer == "higher":
            print(f"{library[index1]["name"]} is higher compared with {library[index2]["name"]}")
            print("====================================================================")
            correct += 1
        elif parameter == 0 and answer == "lower":
            print(f"{library[index1]["name"]} is lower compared with {library[index2]["name"]}")
            print("====================================================================")
            correct += 1
        else:
            print(f"Your score is {correct}")
            question = False

    go = ""
    while go != "yes" and go != "no":
        go = input("Do you want to quit 'yes' or 'no'?: ").lower()

    if go == "yes":
        print("Goodbye")
        game = False
    elif go == "no":
        os.system('cls')
