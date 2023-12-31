from random import randint

library = [
    {"name": "Whatsapp",
     "downloaded": "9.66", },
    {"name": "Facebook",
     "downloaded": "7.57", },
    {"name": "Messenger",
     "downloaded": "5.61", },
    {"name": "TikTok",
     "downloaded": "4.51", },
    {"name": "Instagram",
     "downloaded": "4.14", },
    {"name": "Facebook Lite",
     "downloaded": "2.92", },
    {"name": "SHAREit",
     "downloaded": "2.21", },
    {"name": "Netflix",
     "downloaded": "1.88", },
    {"name": "Snapchat",
     "downloaded": "1.71", },
    {"name": "Telegram",
     "downloaded": "1.63", },
    {"name": "Subway Surfers",
     "downloaded": "1.57", },
    {"name": "Spotify",
     "downloaded": "1.41", },
    {"name": "Free Fire",
     "downloaded": "1.39", },
    {"name": "X",
     "downloaded": "1.38", },
    {"name": "Candy Crush Saga",
     "downloaded": "1.32", },
    {"name": "Skype",
     "downloaded": "1.17", },
    {"name": "MX Player",
     "downloaded": "1.16", },
    {"name": "Viber",
     "downloaded": "1.10", },
    {"name": "My Talking Tom",
     "downloaded": "1.03", },
    {"name": "UC Browser",
     "downloaded": "1.00", },
    ]


def random_number():
    random = randint(0, 19)
    return random


index1 = random_number()
index2 = random_number()
compare = library[index1]["downloaded"]
compared = library[index2]["downloaded"]

parameter = 2

answer = ""
while answer != "higher" and answer != "lower":
    answer = input(f"Does {library[index1]["name"]} is higher compared with {library[index2]["name"]}?\n"
                   f"(Type 'higher' or 'lower'): ").lower()

if compare > compared:
    # print(f"{library[index1]["name"]} is higher compared with {library[index2]["name"]}")
    parameter = 1
elif compare < compared:
    # print(f"{library[index1]["name"]} is lower compared with {library[index2]["name"]}")
    parameter = 0
elif compare == compared:
    print("this is bug")

# correct =
if parameter == 1 and answer == "higher":
    print(f"{library[index1]["name"]} is higher compared with {library[index2]["name"]}")
elif parameter == 0 and answer == "lower":
    print(f"{library[index1]["name"]} is lower compared with {library[index2]["name"]}")
else:
    print("loop stop")
