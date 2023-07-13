# Create a class called QuizBrain.
# Write an __init__() method.
# Initialise the question_number to 0.
# Initialise the question_list to an input.

# asking the questions
# checking if the answer was correct
# checking if we're the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0 
        self.questions_list = q_list
        self.score = 0

    # Retrieve the item at the current question_number from the question_list. 
    # Use the input() function to show the user the Question text and ask for the user's answer.


    def still_has_question(self):
        return self.question_number < len(self.questions_list)
    
        # if self.question_number < len(self.questions_list):
        #     return True
        # else:
        #     False

    # Return a boolean depending on the value of question_number.
    # Use the while loop to show the next question until the end.


    def next_question(self):
        current_question = self.questions_list[self.question_number]
        # current_question.text
        self.question_number += 1 
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1 
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
