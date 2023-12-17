import time


print('''
                        __
                      /` ,\\__
                     |    ).-'
                    / .--'
                   / /
     ,      _.==''`  \\
   .'(  _.='         |
  {   ``  _.='       |
   {    \\`     ;    /
    `.   `'=..'  .='
      `=._    .='
        '-`\\\\`__
            `-._{

''')
print("###===========================###")
print("Welcome to The Carrot Heist")
print("Your objective is to take back the carrot that Wyvern Duck steal from divine farm.\n"
      "Wyvern Duck locate at castle ruin, you need find the carrot at castle without find out by Wyvern Duck.")

stage_one = input(
    "You are finally enter the ruin castle, now there 2 paths ahead which path you take?(left or right)\n")
stage_one.lower()
if stage_one == "right":
    print("The building on right path fall on you.\nGame Over.")
elif stage_one == "left":
    print("You safely pass the path.")
    time.sleep(2)
    print("Now your path have big hole you need to jump to pass\nbut when you peek "
          "there Wyvern Duck passing by on the lower floor.")
    stage_two = input("do you want to jump now or wait and jump later?"
                      "(jump or wait)\n")
    stage_two.lower()
    if stage_two == "wait":
        print("Suddenly Wyvern Duck see above and find out there intruder so he fly to "
              "you and spit his fire breath.\nGame Over.")
    elif stage_two == "jump":
        print("After you jump Wyvern Duck noticing there intruder so he go from his nest to find you,\n"
              "this is your chance you need to fast take back the carrot before he comeback.")
        stage_three = input("You finally arrive to the underground level,\n"
                            "now you need to fast before Wyvern Duck back but there 3 doors\n"
                            "Which one do you open?(red, yellow or blue)\n")
        stage_three.lower()
        if stage_three == "red":
            print("Bad luck on you Wyvern Duck are the inside of red door room and he instantly eat you.\n"
                  "Game Over.")
        elif stage_three == "yellow":
            print("Truth to be true, the yellow door room is full of booby trap and you can't make it,\n"
                  "now sleep forever.\nGame Over.")
        elif stage_three == "blue":
            print("You find out the carrot now you take the carrot.\n"
                  "Congratulation You Win!!!")
            time.sleep(6)
            print("But wait")
            time.sleep(3)
            print("Wyvern Duck find you before you safely leave, now run for your live!!!")
            print("-----------------------------------------------------------------------")
            print('''                
                    _          _
                     \\`.__..--'' `.
                     ( _          ,\\
                    ( <_< < <   `','`.
                     \\ (_< < <    \\   `.
                      `. `----'   (  q _p
                        `-._  _.-' `-(_''\\
                         (_'))--,      `._\\
                            `-._<''')
        else:
            print("Game Over.\nHe find you.")
    else:
        print("Game Over.\nHe find you")
else:
    print("Game Over.\nHe find you")
