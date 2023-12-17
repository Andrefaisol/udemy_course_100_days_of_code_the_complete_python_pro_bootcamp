print("---Welcome to the Tip Calculator---")

bill = input("How many bill you pay? $")
while bill.isalpha():
    print("please only number")
    bill = input("How many bill you pay? ")
bill = float(bill)

percent = input("How many percentage you want to give?(10,12,15) ")
while percent.isalpha():
    print("please only number")
    percent = input("How many percentage you want to give?(10,12,15) ")
percent = float(percent)


people = input("How many people you will split the bill? ")
while people.isalpha():
    print("please only number")
    people = input("How many people you will split the bill? ")
people = float(people)

percentage = 100

try:
    total_percentage = (percent / percentage) * bill
except ZeroDivisionError:
    total_percentage = 0
payment = (bill + total_percentage) / people
payment = float(payment)
print("Each person should pay: ${:.2f}".format(payment))

