# Quiz Game

# 1. Create a Question class with an __init()__ method with two attributes: text and answer attribute
from data import question_data

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

new_q = Question("2+3=5", "False")
print(new_q.text) 

