from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for questions in question_data:
    question_text = (questions["question"])
    question_answer = (questions['correct_answer'])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[1].text)

quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
# if quiz.question_number == len(quiz.question_list):
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")