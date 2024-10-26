from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = Question(data["question"], data["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    user_answer = quiz.next_question()
    quiz.check_answer(question_bank, user_answer)
    quiz.print_result()
quiz.print_final_result()