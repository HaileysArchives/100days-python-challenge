# main.py
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question_bank = [
#     Question(q1, a1),
#     Question(q2, a2),
#     Question(q3, a3),
#     ...
# ]

# 2. Write a for loop to iterate over the question_data. 
# Create a Question object from each entry in question_data.
# Append each Question object to the question_bank.

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # question_text = question_data["text"] => TypeError: list indices must be integers or slices, not str
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

 


