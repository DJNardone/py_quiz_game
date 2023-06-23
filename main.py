from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    ques_text = q["question"]
    ques_answer = q["correct_answer"]
    question = Question(ques_text, ques_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Congratulations, You completed the Quiz!")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")
