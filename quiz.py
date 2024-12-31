"""
  Runs the main loop of the linear equation quiz

  Game consists of multiple rounds where the user solves equations
  User starts with 3 lives and loses one for each incorrect answer
  Game ends when the user runs out of lives or decides to quit after a round

  Tracks:
    - Total score
    - Accuracy
    - Rounds
    - Questions answered

  Displays:
    - Feedback on each answer (correct or wrong)
    - Health bar representing remaining lives

  Returns:
    None
"""

import  time
from    generate_linear_eq  import generate_linear_eq
from    check_answer        import check_answer

def quiz():

  # Initialise variables
  score = 0
  total_questions = 0
  lives = 3
  continue_quiz = "Y"
  q_per_round = 5
  round = 1

  # Start
  time.sleep(0.5)
  print("\nWelcome to the Linear Equation Quiz!")
  time.sleep(2)
  print(f"You have {lives} lives (❤️). Get {lives} questions wrong in a row and the quiz ends.")
  time.sleep(2)
  print("Let's begin Round 1!")
  time.sleep(3)

  while continue_quiz == "Y":
    for _ in range(q_per_round):
      healthbar = "".join(["❤️" for _ in range(lives)])
      equation, solution = generate_linear_eq()

      total_questions += 1

      print(f"\n\nQ{total_questions}) Solve for x:")
      print(f"\n    {equation}\n\n")

      print(f"Lives: {healthbar}")
      user_answer = input("Your answer:\n    x = ")

      if check_answer(user_answer, solution):
        print("\n✅ Correct! 🎉🎉🎉")
        score += 1
        time.sleep(1.5)
      else:
        print(f"\n❌❌❌ Wrong! The correct answer was x = {solution}.")
        lives -= 1
        time.sleep(3)
      if lives <= 0:
        break

    if lives <= 0:
      break
    elif lives > 0:
      round += 1
      continue_quiz = input(f"\nDo you want to continue to Round {round}? (Y/N): ").upper()
      if continue_quiz != 'Y':
        break
      print("\n\n\nRound 2!")
      time.sleep(2)

  # Quiz ends, show final stats
  print("\n--- Quiz Complete! ---\n")
  print(f"  Final Score: { score }/{ total_questions }")
  print(f"  Accuracy: {(score/total_questions)*100:.1f}%")
  print("\nThanks for playing!")
