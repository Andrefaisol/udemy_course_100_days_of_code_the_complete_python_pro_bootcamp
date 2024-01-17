txt = "[name]"
with open("Input/Letters/starting_letter.txt", mode="r") as invite:
    p = invite.read()

with open("Input/Names/invited_names.txt", mode="r") as names:
    namesre = names.readlines()

for i in namesre:
    y = i.strip()
    new_let = p.replace(txt, y)
    with open(f"Output/ReadyToSend/Send_to_{y}.txt", mode="w") as file:
        file.write(new_let)
