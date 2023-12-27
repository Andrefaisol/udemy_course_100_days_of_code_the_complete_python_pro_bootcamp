import random


def draw(hand):
    duraw = random.choice(cards)
    hand.append(duraw)


def calculate(total_hand):
    result = sum(total_hand)
    return result


def ace(result, hand):
    if result > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    else:
        return


def hand_check(hand1, hand2):
    if hand1 == 21:
        if hand1 == hand2:
            print("Draw")
        elif hand1 > hand2:
            while calculate(dealer_hand) < 17:
                draw(dealer_hand)
                print(dealer_hand)
                ace(result=calculate(dealer_hand), hand=dealer_hand)
            if hand1 == calculate(dealer_hand):
                print("Draw")
            else:
                print("You Win")

    elif hand1 > 21:
        print("Dealer Win")

    elif hand1 < 21:
        while calculate(dealer_hand) < 17:
            draw(dealer_hand)
            print(dealer_hand)
            ace(result=calculate(dealer_hand), hand=dealer_hand)
        if calculate(dealer_hand) > 21:
            print("You Win")
        elif hand1 > calculate(dealer_hand):
            print("You Win")
        elif hand1 == calculate(dealer_hand):
            print("Draw")
        else:
            print("Dealer Win")


def draw_again_func():
    draw_again = input("Do you want to draw again?(Press 'y' or 'n'): ").lower()
    while draw_again != "y" and draw_again != "n":
        draw_again = input("Do you want to draw again?(Press 'y' or 'n'): ").lower()
    if draw_again == "y":
        draw(user_hand)
        ace(result=calculate(user_hand), hand=user_hand)
        hand_string = ""
        for x in user_hand:
            hand_string += str(x) + " "
        print(f"Your hand is {hand_string}")
        print(f"total hand value: {calculate(user_hand)}")
        print(f"Dealer hand is {dealer_hand[0]} and ***")
        if calculate(user_hand) < 21:
            draw_again_func()
    else:
        return


# game run start here
blackjack = True
while blackjack:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = []
    dealer_hand = []

    start = input("Press 'Enter' to start")
    while start != "":
        start = input("Press 'Enter' to start")

    for idx in range(2):
        draw(user_hand)
        ace(result=calculate(user_hand), hand=user_hand)
        draw(dealer_hand)
        ace(result=calculate(dealer_hand), hand=dealer_hand)

    sum_user_hand = calculate(user_hand)
    sum_dealer_hand = calculate(dealer_hand)

    print(f"Your hand is {user_hand[0]} and {user_hand[1]}")
    print(f"total hand value: {sum_user_hand}")
    print(f"Dealer hand is {dealer_hand[0]} and ***")

    if sum_user_hand == 21:
        if sum_user_hand == sum_dealer_hand:
            print("")

        elif sum_user_hand > sum_dealer_hand:
            print("")
    else:
        draw_again_func()

    hand_check(hand1=calculate(user_hand), hand2=calculate(dealer_hand))

    sum_user_hand = calculate(user_hand)
    sum_dealer_hand = calculate(dealer_hand)

    hand_string1 = ""
    hand_string2 = ""
    for i in user_hand:
        hand_string1 += str(i) + " "
    for i in dealer_hand:
        hand_string2 += str(i) + " "

    print("")
    print(f"Your hand is {hand_string1}")
    print(f"total hand value: {sum_user_hand}")
    print(f"Dealer hand is {hand_string2}")
    print(f"total hand value: {sum_dealer_hand}")
    print("")
    play_again = input("Do you want to play again?('y' or 'n'): ").lower()
    while play_again != "y" and play_again != "n":
        play_again = input("Do you want to play again?('y' or 'n'): ").lower()
    if play_again == "n":
        print("Good Bye")
        blackjack = False
