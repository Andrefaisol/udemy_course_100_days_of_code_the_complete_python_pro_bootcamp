alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(pesan, parameter):
#     pesan_list = list(pesan)
#     result = ""
#     parameter = int(parameter) % 26
#     for i in pesan_list:
#         x = alphabet.index(i)
#         encode = x + parameter
#         result += alphabet[encode]
#     print("Your encrypted message is:\n{}".format(result))
#
#
# def decrypt(pesan, parameter):
#     pesan_list = list(pesan)
#     result = ""
#     parameter = int(parameter) % 26
#     for i in pesan_list:
#         x = alphabet.index(i)
#         encode = x - parameter
#         result += alphabet[encode]
#     print("Your decrypted message is:\n{}".format(result))

def caesar(pesan, parameter, choice):
    pesan_list = list(pesan)
    result = ""
    new_parameter = int(parameter) % 26
    if choice == "decode":
        new_parameter *= -1
    for i in pesan_list:
        if i in alphabet:
            x = alphabet.index(i)
            encode = x + new_parameter
            if encode > 25:
                encode -= 26
            result += alphabet[encode]
        else:
            result += i
    print("Your {}d message is:\n{}".format(choice,result))


program = True
while program:
    choosing_to_do = input("Type 'encode' to encrypt or type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift = input("Type shift number:\n")

    while choosing_to_do != "encode" and choosing_to_do != "decode":
        choosing_to_do = input("Type 'encode' to encrypt or type 'decode' to decrypt:\n").lower()

    while shift.isalpha():
        print("please insert only round number")
        shift = input("Type shift number:\n")

    caesar(pesan=message, parameter=shift, choice=choosing_to_do)

    asking = input("Do you want to using this program again?(yes/no)\n").lower()
    while asking != "yes" and asking != "no":
        print("answer only 'yes' or 'no'")
        asking = input("Do you want to using this program again?(yes/no)\n").lower()

    if asking == "no":
        print("goodbye")
        program = False
