"""
  This is a linear equation quiz where the user solves randomly generated linear equations in the form:
  `ax + b = c`

  The quiz ends when the user runs out of lives or decides to quit.

  Features:
    - multiple rounds
    - user score tracking
    - lives

  Modules:
    - random: Used to generate random coefficients, constants and solutions for linear equations
    - time: Used for adding delays to improve user experience

  Functions:
    - generate_linear_eq(): Generates a random linear equation along with its solution
    - check_answer(user_answer, correct_answer): Checks if the user's answer is correct
    - quiz(): Main function to run the quiz
"""

from quiz import quiz

if __name__ == "__main__":
  quiz()
