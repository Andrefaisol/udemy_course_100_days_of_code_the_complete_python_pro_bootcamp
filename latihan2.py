name1 = "Angela Yu"
name2 = "Jack Bauer"
name1 = name1.lower()
name2 = name2.lower()
name_together = name1 + name2
alpha_t = name_together.count("t")
alpha_r = name_together.count("r")
alpha_u = name_together.count("u")
alpha_e = name_together.count("e")
alpha_l = name_together.count("l")
alpha_o = name_together.count("o")
alpha_v = name_together.count("v")

word_true = alpha_t + alpha_r + alpha_u + alpha_e
word_love = alpha_l + alpha_o + alpha_v + alpha_e

score = str(word_true) + str(word_love)

if int(score) < 10 or int(score) > 90:
    print("Your score is {}, you go together like coke and mentos.".format(score))
elif int(score) < 50 and int(score) > 40:
    print("Your score is {}, you are alright together.".format(score))
else:
    print("Your score is {}.".format(score))