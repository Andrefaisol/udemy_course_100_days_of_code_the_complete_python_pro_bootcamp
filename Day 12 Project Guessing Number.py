import random
import os

CHOSE_NUMBER = random.randint(1, 100)
EASY = 10
HARD = 5


def input_level():
    level = input("Choose what level do you want to play, type 'easy' or 'hard': ").lower()
    while level != "easy" and level != "hard":
        level = input("Choose what level do you want to play, type 'easy' or 'hard': ").lower()
    return level


def level_check(level):
    global EASY
    global HARD
    count = 0
    if level == "easy":
        count += EASY
    elif level == "hard":
        count += HARD
    return count


def guessing():
    number_guess = ""
    while not number_guess.isdigit() or (int(number_guess) < 1 or int(number_guess) > 100):
        number_guess = input("Type your number guess here: ")
    return int(number_guess)


def is_it_right(number):
    global CHOSE_NUMBER
    if number < CHOSE_NUMBER:
        print("too low")
    elif number > CHOSE_NUMBER:
        print("too high")


game = True
while game:
    print('''                                                                                                                 
                                                                               ,--.                              
  ,----..                                                                    ,--.'|                       ____   
 /   /   \\                                                               ,--,:  : |                     ,'  , `. 
|   :     :          ,--,                                             ,`--.'`|  ' :         ,--,     ,-+-,.' _ | 
.   |  ;. /        ,'_ /|             .--.--.    .--.--.              |   :  :  | |       ,'_ /|  ,-+-. ;   , || 
.   ; /--`    .--. |  | :    ,---.   /  /    '  /  /    '             :   |   \\ | :  .--. |  | : ,--.'|'   |  || 
;   | ;  __ ,'_ /| :  . |   /     \\ |  :  /`./ |  :  /`./             |   : '  '; |,'_ /| :  . ||   |  ,', |  |, 
|   : |.' .'|  ' | |  . .  /    /  ||  :  ;_   |  :  ;_               '   ' ;.    ;|  ' | |  . .|   | /  | |--'  
.   | '_.' :|  | ' |  | | .    ' / | \\  \\    `. \\  \\    `.            |   | | \\   ||  | ' |  | ||   : |  | ,     
'   ; : \\  |:  | : ;  ; | '   ;   /|  `----.   \\ `----.   \\       ___ '   : |  ; .':  | : ;  ; ||   : |  |/      
'   | '/  .''  :  `--'   \'   |  / | /  /`--'  //  /`--'  /    .'  .`||   | '`--'  '  :  `--'   \\   | |`-'       
|   :    /  :  ,      .-./|   :    |'--'.     /'--'.     /  .'  .'   :'   : |      :  ,      .-./   ;/           
 \\   \\ .'    `--`----'     \\   \\  /   `--'---'   `--'---',---, '   .' ;   |.'       `--`----'   '---'            
  `---`                     `----'                       ;   |  .'    '---'                                      
                                                         `---'                                                   ''')

    print("=============================================================")
    many_guess = level_check(input_level())
    answer = 0

    while answer != CHOSE_NUMBER:

        if many_guess == 0:
            print("============================")
            print("You run out of guess attempt")
            print("============================")
            break

        print(f"You have {many_guess} more attempt to guess")
        answer = guessing()
        is_it_right(answer)
        many_guess -= 1
        print("")

    if answer == CHOSE_NUMBER:
        print("==========================")
        print("Your guess number is right")
        print("==========================")

    play_again = input("Do you want to play again?(Type 'y' or 'n'): ").lower()
    while play_again != "y" and play_again != "n":
        play_again = input("Do you want to play again?(Type 'y' or 'n'): ").lower()

    if play_again == "n":
        print("")
        print("Goodbye")
        game = False
    else:
        os.system("cls")
