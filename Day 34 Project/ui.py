from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Trivia")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "normal"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, highlightthickness=1, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=290,
            text="try this",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_pic = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_pic, command=self.button_true)
        self.true_button.grid(row=2, column=0)

        self.false_pic = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_pic, command=self.button_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reach end of question")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def button_true(self):
        answer = "True"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def button_false(self):
        answer = "False"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
