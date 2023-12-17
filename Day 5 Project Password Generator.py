import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*', '+']

pass_length = int(input("How many characters do you want in your password?\n"))
num_length = int(input("How many numbers do you want in your password?\n"))
symbols_length = int(input("How many symbols do you want in your password?\n"))

# password = ""
# for i in range(1, pass_length + 1):
#     ran_letters = random.choice(letters)
#     password += ran_letters
# for i in range(1, num_length + 1):
#     ran_numbers = random.choice(numbers)
#     password += ran_numbers
# for i in range(1, symbols_length + 1):
#     ran_symbols = random.choice(symbols)
#     password += ran_symbols
# print(password)

password = []
for i in range(1, pass_length + 1):
    ran_letters = random.choice(letters)
    password.append(ran_letters)
for i in range(1, num_length + 1):
    ran_numbers = random.choice(numbers)
    password.append(ran_numbers)
for i in range(1, symbols_length + 1):
    ran_symbols = random.choice(symbols)
    password.append(ran_symbols)
random.shuffle(password)

final_password = ""
for i in password:
    final_password += i
print("Your password is: {}".format(final_password))

