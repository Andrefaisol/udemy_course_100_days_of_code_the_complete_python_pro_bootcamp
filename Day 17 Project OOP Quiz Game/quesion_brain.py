# TODO: 1. asking question
# TODO: 2. check if the answer correct
# TODO: 3. check if we at end of quiz

class QuizBrain:
    def __init__(self, bank):
        self.question_number = 0
        self.question_list = bank
        self.score = 0

    def next_question(self):
        answer = ""
        number_quiz = 1 + self.question_number
        while answer != "True" and answer != "False":
            answer = input(f"Q.{number_quiz}: {self.question_list[self.question_number].text} "
                           f"answer('True' or 'False'): ").capitalize()
        self.check_answer(answer)
        self.question_number += 1

    def last_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, y):
        if y == self.question_list[self.question_number].answer:
            self.score += 1
            print(f"Yes You right the answer is '{y}'")
            print(f"Score:\n{self.score}/{self.question_number + 1}")
        else:
            print(f"You wrong the answer is '{self.question_list[self.question_number].answer}'")
            print(f"Score:\n{self.score}/{self.question_number + 1}")
