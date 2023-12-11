from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
quiz = QuizzBrain(question_bank)


for item in question_data:
    question = item['question']
    answer = item['correct_answer']
    new_q = Question(question, answer)
    question_bank.append(new_q)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
quiz_score_percent = round((quiz.score / quiz.question_number) * 100)
print(f"Your final score was {quiz.score}/{quiz.question_number} with a {quiz_score_percent}%.")