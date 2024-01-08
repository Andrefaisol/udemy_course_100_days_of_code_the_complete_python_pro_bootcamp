
MENU = ["espresso", "americano", "latte", "cappuccino", ]
PRICE = {"espresso": 1.50, "americano": 2.00, "latte": 2.50, "cappuccino": 3.00}


class MachineCoffe:
    def __init__(self, menu, price):
        self.menu = menu
        self.price = price

    def resource_report(self, water, coffe, milk):
        print(f"Remaining resource:\nWater: {water}ml\nCoffe: {coffe}g\nMilk:  {milk}ml")

    def resource_check(self, water, coffe, milk, command):
        back_to_user_input = command
        if command == "espresso":
            if water < 50 or coffe < 18:
                print("=========================================================")
                print("Water or Coffe not enough, please add some water or coffe")
                print("=========================================================")
                back_to_user_input = ""
        elif command == "latte":
            if water < 200 or coffe < 24 or milk < 150:
                print("=====================================================================")
                print("Water, Coffe or milk not enough, please add some water, coffe or milk")
                print("=====================================================================")
                back_to_user_input = ""
        elif command == "americano":
            if water < 200 or coffe < 18:
                print("=======================================================")
                print("Water, Coffe not enough, please add some water or coffe")
                print("=======================================================")
                back_to_user_input = ""
        elif command == "latte":
            if water < 250 or coffe < 24 or milk < 100:
                print("=====================================================================")
                print("Water, Coffe or milk not enough, please add some water, coffe or milk")
                print("=====================================================================")
                back_to_user_input = ""
        return back_to_user_input

    def cent_to_dollar(self, cent):
        dollar = cent / 100
        return dollar

    def converter(self, w, x, y, z):
        total = w + (x * 5) + (y * 10) + (z * 25)
        return total

    def insert_money(self):
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
        total = self.cent_to_dollar(self.converter(w=int(penny), x=int(nickel), y=int(dime), z=int(quarter)))
        return total

    def coffe_on_ready(self):
        money = 0
        user_input = ""
        back_to = "a"
        global water_vol
        global coffe_vol
        global milk_vol
        print("Coffe machine ready, please order your coffe")
        while user_input not in MENU:
            if user_input == "report":
                self.resource_report(water=water_vol, coffe=coffe_vol, milk=milk_vol)
            elif user_input == "turn off":
                break
            user_input = input("coffe list : espresso, americano, latte, cappuccino\n"
                               "to inspect resource type 'report'\n"
                               "to turn off type 'turn off'\n"
                               "What would you like?: ").lower()
            if user_input in MENU:
                user_input = self.resource_check(water=water_vol, coffe=coffe_vol, milk=milk_vol, command=user_input)
        print("================================================================")
        if user_input == "turn off":
            print("Goodbye")
            return money, user_input
        elif user_input in MENU:
            while money < PRICE[user_input]:
                print(f"{user_input} price is ${PRICE[user_input]}, please insert your amount money to proceed")
                money = self.insert_money()
                if money < PRICE[user_input]:
                    print(f"{user_input} price is ${PRICE[user_input]} your money is not enough")
                    print("You get refund ${:.2f}".format(money))
                    print("================================================================")
                    money = 0
                    while back_to != "back" and back_to != "":
                        back_to = input("Would you like to reinsert money or change order?\n"
                                        "type 'back' to change order or press enter to reinsert money: ").lower()
                    if back_to == "back":
                        break
        if back_to == "back":
            money, user_input = self.coffe_on_ready()
        return money, user_input

    def make_espresso(self, water, coffe):
        water_cap = water
        coffe_cap = coffe

        water_cap -= 50
        coffe_cap -= 18
        return water_cap, coffe_cap

    def make_latte(self, water, coffe, milk):
        water_cap = water
        coffe_cap = coffe
        milk_cap = milk

        water_cap -= 200
        coffe_cap -= 24
        milk_cap -= 150
        return water_cap, coffe_cap, milk_cap

    def make_americano(self, water, coffe):
        water_cap = water
        coffe_cap = coffe

        water_cap -= 200
        coffe_cap -= 18
        return water_cap, coffe_cap

    def make_cappuccino(self, water, coffe, milk):
        water_cap = water
        coffe_cap = coffe
        milk_cap = milk

        water_cap -= 250
        coffe_cap -= 24
        milk_cap -= 100
        return water_cap, coffe_cap, milk_cap


cafe3000 = MachineCoffe(MENU, PRICE)

water_vol = 1000
coffe_vol = 200
milk_vol = 500
machine = True
while machine:
    uang, perintah = cafe3000.coffe_on_ready()

    if perintah == "turn off":
        break
    elif perintah == "espresso":
        water_vol, coffe_vol = cafe3000.make_espresso(water=water_vol, coffe=coffe_vol)
    elif perintah == "americano":
        water_vol, coffe_vol = cafe3000.make_americano(water=water_vol, coffe=coffe_vol)
    elif perintah == "latte":
        water_vol, coffe_vol, milk_vol = cafe3000.make_latte(water=water_vol, coffe=coffe_vol, milk=milk_vol)
    elif perintah == "cappuccino":
        water_vol, coffe_vol, milk_vol = cafe3000.make_cappuccino(water=water_vol, coffe=coffe_vol, milk=milk_vol)
    print("================================================================")
    print(f"Here your {perintah}!")
    print("================================================================")
    if uang > PRICE[perintah]:
        print(f"Your total money is ${uang}")
        uang -= PRICE[perintah]
        print("Here your change ${:.2f}".format(uang))
    print("================================================================")
    cafe3000.resource_report(water=water_vol, coffe=coffe_vol, milk=milk_vol)
    print("================================================================")
