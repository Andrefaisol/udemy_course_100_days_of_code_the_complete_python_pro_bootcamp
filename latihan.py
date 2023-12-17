print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
pizza_price = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
if size == "S":
    pizza_price = small_pizza

elif size == "M":
    pizza_price = medium_pizza

elif size == "L":
    pizza_price = large_pizza

if add_pepperoni == "Y":
    if size == "S":
        pizza_price += 2
    else:
        pizza_price += 3

if extra_cheese == "Y":
    pizza_price += 1

print("Your final bill is: ${}.".format(pizza_price))
