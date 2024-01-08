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
answer_list = []
for number in range(len(question_bank)):
    answer_list.append(quiz.next_question(number))
    print(answer_list)
