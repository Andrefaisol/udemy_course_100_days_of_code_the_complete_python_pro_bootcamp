from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_FRENCH = "French"
LANG_ENG = "English"
cur_data = {}
data_list = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_list = original_data.to_dict(orient="records")
else:
    data_list = data.to_dict(orient="records")


def start():
    global cur_data, flip_timer
    window.after_cancel(flip_timer)
    ran_num = random.randint(0, len(data_list) - 1)
    cur_data = data_list[ran_num]
    ran_lang = cur_data[LANG_FRENCH]
    canvas.itemconfig(language_card, text=ran_lang)
    canvas.itemconfig(title_card, text=LANG_FRENCH)
    canvas.itemconfig(card_color, image=f_card)
    flip_timer = window.after(3000, translate)


def translate():
    canvas.itemconfig(card_color, image=b_card)
    canvas.itemconfig(title_card, text=LANG_ENG)
    canvas.itemconfig(language_card, text=cur_data[LANG_ENG])


def is_known():
    data_list.remove(cur_data)
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    start()


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=translate)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
f_card = PhotoImage(file="images/card_front.png")
b_card = PhotoImage(file="images/card_back.png")
card_color = canvas.create_image(400, 263, image=f_card)

title_card = canvas.create_text(400, 150, fill="black", text="", font=("Ariel", 40, "italic"))
language_card = canvas.create_text(400, 263, fill="black", text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

know_card = PhotoImage(file="images/right.png")
idk_card = PhotoImage(file="images/wrong.png")
know_button = Button(image=know_card, highlightthickness=0, command=start)
idk_button = Button(image=idk_card, highlightthickness=0, command=is_known)
know_button.grid(row=1, column=1)
idk_button.grid(row=1, column=0)

start()

window.mainloop()
