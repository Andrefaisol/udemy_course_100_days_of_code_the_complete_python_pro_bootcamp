from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_check.config(text="")
    label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label.config(text="Long Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_min < 1:
        if count_sec < 10:
            count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✅︎"
        label_check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=208, height=228, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(104, 114, image=tomato)
timer_text = canvas.create_text(104, 135, text="00.00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "normal"))
label.grid(column=1, row=0)
label_check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
label_check.grid(column=1, row=3)
button_start = Button(text="Start", command=start, font=(FONT_NAME, 12, "normal"))
button_start.grid(column=0, row=2)
button_reset = Button(text="Reset", command=reset, font=(FONT_NAME, 12, "normal"))
button_reset.grid(column=2, row=2)

window.mainloop()
