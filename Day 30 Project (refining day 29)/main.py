from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password_entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    new_dict = {
        web_entry.get(): {
            "email": eu_entry.get(),
            "password": password_entry.get(),
        }
    }
    if len(eu_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Hei!", message="You left email or password empty please fill it before submit")
    else:
        ask_sure = messagebox.askokcancel(title=f"Platform: {web_entry.get()}",
                                          message=f"Are these entry correct?\nEmail/Username: {eu_entry.get()}"
                                                  f"\nPassword: {password_entry.get()}")

        if ask_sure:
            with open(file="saved_data.json", mode="r") as file:
                new_data = json.load(file)
                new_data.update(new_dict)

            with open(file="saved_data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)

            web_entry.delete(0, END)
            eu_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=25)


image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:", font=("Helvetica", 14, "normal"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("Helvetica", 14, "normal"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Helvetica", 14, "normal"))
password_label.grid(row=3, column=0)


generate_button = Button(text="Generate Password", font=("Helvetica", 10, "normal"), width=14, command=generate)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", font=("Helvetica", 10, "normal"), command=add, width=39)
add_button.grid(row=4, column=1, columnspan=2)


web_entry = Entry(width=35, font=("Helvetica", 12, "normal"))
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

eu_entry = Entry(width=35, font=("Helvetica", 12, "normal"))
eu_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21, font=("Helvetica", 12, "normal"))
password_entry.grid(row=3, column=1)

window.mainloop()
