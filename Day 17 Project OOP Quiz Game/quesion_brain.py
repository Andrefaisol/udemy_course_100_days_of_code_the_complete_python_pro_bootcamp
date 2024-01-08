# TODO: 1. asking question
# TODO: 2. check if the answer correct
# TODO: 3. check if we at end of quiz

class QuizBrain:
    def __init__(self, bank):
        self.question_number = 0
        self.question_list = bank

    def next_question(self, number):
        self.question_number += number
        answer = ""
        number_quiz = 1 + number
        while not answer.isalpha():
            answer = input(f"Q.{number_quiz}: {self.question_list[self.question_number].text} "
                           f"answer('True' or 'False'): ").capitalize()
        return answer

    def last_question(self):
        pass
