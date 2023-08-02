class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_question(self):
        list_len = len(self.question_list)
        return list_len > self.question_number

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {question.text} (True/False)")
        self.check_answer(question, player_answer)

    def check_answer(self, question, p_answer):
        q_answer = question.answer
        if p_answer.lower() == q_answer.lower():
            print("Right answer.")
            self.score += 1
        else:
            print("Wrong answer.")
        print(f"The correct answer is {q_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
