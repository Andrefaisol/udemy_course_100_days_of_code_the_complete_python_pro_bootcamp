import random
rock = 1
paper = 2
scissor = 3
hand_list = [rock, paper, scissor]

def rock_paper_scissor():

    random_hand = random.choice(hand_list)

    my_hand = input("what your choice?(input 1 for rock, 2 for paper, 3 for scissor)\n")
    while my_hand.isalpha():
        my_hand = input("what your choice?(input 1 for rock, 2 for paper, 3 for scissor)\n")
    my_hand = int(my_hand)

    print("Computer choice:")

    if random_hand == 1:
        print("Com choose rock")
    elif random_hand == 2:
        print("Com choose paper")
    elif random_hand == 3:
        print("Com choose scissor")
    print("")
    print("VS")
    print("")
    print("Your choice:")
    if my_hand == 1:
        print("You choose rock")
    elif my_hand == 2:
        print("You choose paper")
    elif my_hand == 3:
        print("You choose scissor")

    if (my_hand == 1 and random_hand == 3) or (my_hand == 2 and random_hand == 1) or (my_hand == 3 and random_hand == 2):
        print("You Win!")
    elif (my_hand == 1 and random_hand == 2) or (my_hand == 2 and random_hand == 3) or (my_hand == 3 and random_hand == 1):
        print("You Lose!")
    else:
        print("Tie!")

    again = input("do you want to play again?(Y/N)\n").lower()
    if again != "n":
        rock_paper_scissor()

rock_paper_scissor()