"""
  Checks if the user's answer is correct

  Compares user answer to the correct solution for the equation
  Handles invalid input, accounting for minor floating-point inaccuracies

  Args:
    user_answer (str): the user's answer as a string
    correct_answer (int): the correct solution for `x`

  Returns:
    bool: True if the user's answer is correct, otherwise False
"""

def check_answer(user_answer, correct_answer):

  try:
    user_answer = float(user_answer)
    if abs(user_answer - correct_answer) < 0.01:  # Account for minute floating-point differences if needed
      return True
    return False
  except ValueError:
    return False
