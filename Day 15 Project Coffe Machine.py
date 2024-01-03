
MENU = ["espresso", "americano", "latte", "cappuccino",]


def resource_report(water, coffe, milk):
    print(f"Remaining resource:\nWater: {water}ml\nCoffe: {coffe}g\nMilk:  {milk}ml")


def resource_check(water, coffe, milk, command):
    global user_command
    if command == "espresso":
        if water < 50 or coffe < 18:
            print("Water or Coffe not enough, please add some water or coffe")
            user_command = ""
    elif command == "latte":
        if water < 200 or coffe < 24 or milk < 150:
            print("Water, Coffe or milk not enough, please add some water, coffe or milk")
            user_command = ""
    else:
        return water, coffe, milk
    return water, coffe, milk


water_capacity = 1000
coffe_capacity = 200
milk_capacity = 500
machine_coffe_on = True
while machine_coffe_on:
    money = 0
    user_command = ""
    while user_command not in MENU:
        if user_command == "report":
            resource_report(water=water_capacity, coffe=coffe_capacity, milk=milk_capacity)
        elif user_command == "turn off":
            break
        user_command = input("What would you like? (espresso, americano, latte, cappuccino): ").lower()
        if user_command in MENU:
            resource_check(water=water_capacity, coffe=coffe_capacity, milk=milk_capacity, command=user_command)
    if user_command == "turn off":
        print("Goodbye")
        break
    elif user_command == "espresso":
        water_capacity -= 50
        coffe_capacity -= 18
        print("Here your espresso")
        resource_report(water=water_capacity, coffe=coffe_capacity, milk=milk_capacity)
    elif user_command == "latte":
        water_capacity -= 200
        coffe_capacity -= 24
        milk_capacity -= 150
        print("Here your latte")
        resource_report(water=water_capacity, coffe=coffe_capacity, milk=milk_capacity)
    print("================================================================")
