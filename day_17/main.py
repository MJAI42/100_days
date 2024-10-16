from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = Question(data["text"], data["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
list_len = len(question_bank)
score = 0
print("\n" * 100)

while quiz.question_number < list_len:
    user_answer = quiz.next_question()
    answer = question_bank[quiz.question_number].answer

    if answer == user_answer:
        score += 1
        quiz.question_number += 1
        print("You got it right!")
        print(f"The correct answer was: {answer}")
        print(f"You current score is: {score}/{quiz.question_number}")
        print("\n"*3)
        
    else:
        quiz.question_number += 1
        print("You got it wrong!")
        print(f"The correct answer was: {answer}")
        print(f"You current score is: {score}/{quiz.question_number}")
        print("\n"*3)