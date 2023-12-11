class QuizzBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        print(self.question_list)


    def still_has_questions(self):
        """Returns True if there are still questions left to answer, and returns False when all questions have been asked."""
        return self.question_number < len(self.question_list)
        # the return statement is the same as the below if statement
            # if self.question_number < len(self.question_list):
            #     return True
            # else:
            #     return False
        
    def next_question(self):
        """Shows the current question and prompts to user for their answer."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} Type 'True' or 'False': ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Takes in the "User Input, and the Correct Answer and compares the two. Printing to the screen if it was right or wrong, and what the correct answer was."""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()