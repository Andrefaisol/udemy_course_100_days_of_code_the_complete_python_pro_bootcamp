
MENU = ["espresso", "americano", "latte", "cappuccino",]
PRICE = {"espresso": 1.50, "americano": 2.00, "latte": 2.50, "cappuccino": 3.00}


def resource_report(water, coffe, milk):
    print(f"Remaining resource:\nWater: {water}ml\nCoffe: {coffe}g\nMilk:  {milk}ml")


def resource_check(water, coffe, milk, command):
    global perintah
    if command == "espresso":
        if water < 50 or coffe < 18:
            print("=========================================================")
            print("Water or Coffe not enough, please add some water or coffe")
            print("=========================================================")
            perintah = ""
    elif command == "latte":
        if water < 200 or coffe < 24 or milk < 150:
            print("=====================================================================")
            print("Water, Coffe or milk not enough, please add some water, coffe or milk")
            print("=====================================================================")
            perintah = ""
    elif command == "americano":
        if water < 200 or coffe < 18:
            print("=======================================================")
            print("Water, Coffe not enough, please add some water or coffe")
            print("=======================================================")
            perintah = ""
    elif command == "latte":
        if water < 250 or coffe < 24 or milk < 100:
            print("=====================================================================")
            print("Water, Coffe or milk not enough, please add some water, coffe or milk")
            print("=====================================================================")
            perintah = ""
    else:
        return water, coffe, milk
    return water, coffe, milk


def cent_to_dollar(cent):
    dollar = cent / 100
    return dollar


def converter(w, x, y, z):
    total = w + (x * 5) + (y * 10) + (z * 25)
    return total


def insert_money():
    penny = ""
    nickel = ""
    dime = ""
    quarter = ""
    while not penny.isdigit():
        penny = input("How many penny do you insert: ")
    while not nickel.isdigit():
        nickel = input("How many nickel do you insert: ")
    while not dime.isdigit():
        dime = input("How many dime do you insert: ")
    while not quarter.isdigit():
        quarter = input("How many quarter do you insert: ")
    total = cent_to_dollar(converter(w=int(penny), x=int(nickel), y=int(dime), z=int(quarter)))
    return total


def coffe_on_ready():
    money = 0
    user_command = ""
    back_to = "a"
    print("Coffe machine ready, please order your coffe")
    while user_command not in MENU:
        if user_command == "report":
            resource_report(water=water_capacity, coffe=coffe_capacity, milk=milk_capacity)
        elif user_command == "turn off":
            break
        user_command = input("coffe list : espresso, americano, latte, cappuccino\n"
                             "to inspect resource type 'report'\n"
                             "to turn off type 'turn off'\n"
                             "What would you like?: ").lower()
        if user_command in MENU:
            resource_check(water=water_capacity, coffe=coffe_capacity, milk=milk_capacity, command=user_command)
    print("================================================================")
    if user_command == "turn off":
        print("Goodbye")
        return money, user_command
    elif user_command in MENU:
        while money < PRICE[user_command]:
            print(f"{user_command} price is ${PRICE[user_command]}, please insert your amount money to proceed")
            money = insert_money()
            if money < PRICE[user_command]:
                print(f"{user_command} price is ${PRICE[user_command]} your money is not enough")
                print("You get refund ${:.2f}".format(money))
                print("================================================================")
                money = 0
                while back_to != "back" and back_to != "":
                    back_to = input("Would you like to reinsert money or change order?\n"
                                    "type 'back' to change order or press enter to reinsert money: ").lower()
                if back_to == "back":
                    break
    if back_to == "back":
        money, user_command = coffe_on_ready()
    return money, user_command


water_capacity = 1000
coffe_capacity = 200
milk_capacity = 500
machine_coffe_on = True
while machine_coffe_on:
    uang, perintah = coffe_on_ready()

    if perintah == "turn off":
        break
    elif perintah == "espresso":
        water_capacity -= 50
        coffe_capacity -= 18
    elif perintah == "americano":
        water_capacity -= 200
        coffe_capacity -= 18
    elif perintah == "latte":
        water_capacity -= 200
        coffe_capacity -= 24
        milk_capacity -= 150
    elif perintah == "cappuccino":
        water_capacity -= 250
        coffe_capacity -= 24
        milk_capacity -= 100
    print("================================================================")
    print(f"Here your {perintah}!")
    print("================================================================")
    if uang > PRICE[perintah]:
        print(f"Your total money is ${uang}")
        uang -= PRICE[perintah]
        print("Here your change ${:.2f}".format(uang))
    print("================================================================")
    resource_report(water=water_capacity, coffe=coffe_capacity, milk=milk_capacity)
    print("================================================================")
