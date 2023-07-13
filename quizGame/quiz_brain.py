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
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
