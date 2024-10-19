class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        switch = True
        while switch:
            user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True / False)")
            user_answer = user_answer.title()
            if user_answer == "True" or user_answer == "False":
                switch = False
                return user_answer
            else:
                print("I did not understand can you please try again.")
    
    def check_answer(self, question_bank, user_answer):
        counter = self.question_number
        answer = self.question_list[counter].answer
        if answer == user_answer:
            print("You got it right!")
            print(f"The correct answer was: {answer}")
            self.question_number += 1
            return 1
        else:
            print("You got it wrong!")
            print(f"The correct answer was: {answer}")
            self.question_number += 1
            return 0
        
    def print_result(self, score):
        print(f"You current score is: {score}/{self.question_number}")
        print("\n"*3)