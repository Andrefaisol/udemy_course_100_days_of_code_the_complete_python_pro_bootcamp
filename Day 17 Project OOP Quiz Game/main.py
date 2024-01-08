from data import question_data
from question_model import Question
from quesion_brain import QuizBrain

question_bank = []
for i in question_data:
    question_t = i["text"]
    answer_t = i["answer"]
    new_question = Question(question_t, answer_t)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.last_question():
    quiz.next_question()
print("==============================")
print("You completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
print("==============================")
