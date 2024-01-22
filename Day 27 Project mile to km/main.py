from tkinter import *


def clickme():
    n = input_word.get()
    m = round(int(n) * 1.6, 1)
    label2.config(text=m)


window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

label0 = Label(text="is equal to", font=("Helvetica", 18, "normal"))
label0.grid(column=0, row=1)

input_word = Entry(width=10)
input_word.grid(column=3, row=0)

label = Label(text="Miles", font=("Helvetica", 18, "normal"))
label.grid(column=4, row=0)

button = Button(text="Calculate", command=clickme)
button.grid(column=3, row=2)

label2 = Label(text="0", font=("Helvetica", 18, "normal"))
label2.grid(column=3, row=1)

label3 = Label(text="Km", font=("Helvetica", 18, "normal"))
label3.grid(column=4, row=1)
window.mainloop()
