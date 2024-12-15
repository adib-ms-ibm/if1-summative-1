# User Manual

## Introduction:
Welcome to the **Linear Equation Quiz**! This is a fun little game made for educational purposes as part of my **Summative 1** for **Intensive Foundations of Computer Science and Programming - I**.

This is a simple interactive quiz where you solve randomly generated linear equations of the form `ax + b = c`. This game aims to test your foundational math skills through several rounds of quizzing as it keeps track of both your score and accuracy. The quiz will end when you run out of lives or decide not to continue.

Enjoy!

---

## Getting Started:

### Requirements:
This program runs on any computer that has Python installed. No prior Python knowledge is required to play.

### Installation:
1. Ensure that you have Python 3.6 or higher installed on your system.
2. Clone this repo locally by running:
  ```
    git clone https://github.com/adib-ms-ibm/if1-summative-1.git
  ```
- You may also download the program files as a zip if you wish in a single folder.

### Running the Program:
1. Open a terminal or command prompt.
2. Navigate to the folder containing the program files:
  ```
    cd {path_to_folder}/if1-summative-1
  ```
3. Run the command:
  ```
    python main.py
  ```

---

## Tutorial on how to play this game:

### Objective:
You are to solve as many linear equations as you possibly can in order to achieve a high score while avoiding running out of lives. There is no time limit, so do the best you can!

### Game Rules:
- You start out with **3 lives**, denoted by the heart icons (❤️).
- Each incorrect answer costs you a life.
- You lose if your lives reach zero, terminating the quiz.
- You can choose to continue or quit after each round.

### Gameplay:
1. After starting the game, you will be gradually prompted by a series of welcome messages and assigned 3 lives.
2. Each round consists of 5 equations. For example:
   ```
   Solve for x:

   2x + 3 = 7
   ```
3. Type in your solution for `x` (e.g. `2`, `5` etc.).
4. The quiz will tell you if your answer is correct or incorrect.
5. Your remaining lives and score will be displayed after each question for your reassurance.
6. After each round, you can decide whether to continue or not.

### Example Interaction:
```
Welcome to the Linear Equation Quiz!
You have 3 lives (❤️). Get 3 questions wrong in a row and the quiz ends.
Let's begin Round 1!

Q1) Solve for x:

   3x - 2 = 7

Lives: ❤️❤️❤️
Your answer:
    x = 3
✅ Correct! 🎉🎉🎉

Do you want to continue to Round 2? (Y/N): N

--- Quiz Complete! ---
  Final Score: 1/1
  Accuracy: 100.0%
Thanks for playing!
```

---

## Features:

### Randomized Equations
- Each question generates a unique equation to ensure that the game stays dynamic, engaging and challenging.

### Feedback
- Immediate feedback on whether your answer is correct.
- Displays the correct solution if your answer is wrong.

### Health Bar
- A visual representation of your remaining lives, displayed as hearts (❤️).

### Endgame Statistics
- At the very end of the quiz, an output of your score, total questions answered and your accuracy as a percentage will be displayed.

---

## Tips for Success:
- Brush up on your solving linear equations skills if you're unfamiliar with the process.
- Pay close attention to the order of terms and signs (`+` and `-`) in the equation.
- Use a calculator for precision if it is needed.

---

# Technical Documentation:

## Overview:
This program consists of four Python modules:
- `main.py` - serves as the entry point of the program
- `quiz.py` - manages the game loop and user interactions
- `generate_linear_eq.py` - generates the random linear equations
- `check_answer.py` - validates the user's answers

---

## Function Descriptions:

### `generate_linear_eq()`
- **Purpose**: generates a random linear equation along with its solution
- **Input**: none
- **Output**:
  - `equation` (str): the formatted equation
  - `solution` (int): the correct value of `x`
- **Example**:
  ```
  Equation: "2x + 3 = 7"
  Solution: 2
  ```

### `check_answer(user_answer, correct_answer)`
- **Purpose**: validates the user’s answer.
- **Input**:
  - `user_answer` (str): the answer provided by the user
  - `correct_answer` (int): the correct value of `x`
- **Output**: returns `True` (boolean) if the answer is correct, otherwise `False` (boolean)
- **Error Handling**: handles invalid inputs (e.g. non-numeric responses)

### `quiz()`
- **Purpose**: manages the main game loop
- **Input**: none
- **Output**: none
- **Process**:
  1. Initialize variables for score, lives, and round
  2. Generate and displays equations in each round
  3. Track user’s score and feedback
  4. End the game when lives reach zero or the user decides to quit

---

## Code Flow:
1. **Start the Program**:
   - `main.py` calls `quiz()`
2. **Run the Quiz**:
   - `quiz.py` handles the interal game logic and interacts with the user
3. **Generate Equations**:
   - `generate_linear_eq.py` creates random equations for each question
4. **Check Answers**:
   - `check_answer.py` validates the user's input
5. **End the Game**:
   - `quiz.py` displays the final score and accuracy

---

## Error Handling:
- **Invalid Inputs**: non-numeric responses are detected and marked as incorrect
- **Edge Cases**: ensures coefficients like `0x` are omitted/avoided during the equation synthesis step

---

## Customization:
There is some flexibility to this program if the user wishes to alter the script:
- **Number of Lives**: Modify the `lives` variable in `quiz.py`.
- **Questions Per Round**: Adjust the `q_per_round` variable in `quiz.py`.

---

## Future Enhancements:
- Add support for more complex equations (e.g., quadratic equations)
- Implement a leaderboard to track high scores
- Add a timer for each question to increase difficulty
- Allow user to choose number of lives
- Allow user to choose questions per round

---

## Closing Remarks:
The Linear Equation Quiz is a simple yet engaging program that tests the users’ math skills. It is designed to be easy to use while providing insightful feedback and progress tracking. Have fun solving equations and improving your math proficiency!