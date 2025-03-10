"""
    Simple Python Trivia Game
"""

import random

python_questions = {
    "What is the keyword used to define a function in Python?": "def",
    "How do you print something in Python?": "print",
    "What data type is the result of 3 / 2 in Python 3?": "float",
    "How do you get the length of a list in Python?": "len",
    "What symbol is used for single-line comments in Python?": "#",
    "How do you create a list in Python?": "list",
    "What function is used to get user input in Python?": "input",
    "How do you check the data type of a variable in Python?": "type",
    "What keyword is used to create a loop that iterates over items in a list?": "for",
    "How do you check if a key exists in a dictionary?": "in"
}

def python_trivia_game():
    """
        This is the start point of the game

        Returns:
            Nothing
    """
    questions_list = list(python_questions.keys())
    total_questions = 5
    score = 0
    correct_count = 0

    selected_questions = random.sample(questions_list, total_questions)

    for index, question in enumerate(selected_questions):
        print(f'{index + 1}. {question}')
        user_answer = input("Your Answer: ").lower().strip()
        correct_answer = python_questions[question]

        if user_answer == correct_answer.lower():
            print("Correct! \n")
            score += 10
            correct_count += 1
        else:
            print(f"Wrong. The correct answer is : {correct_answer} \n")

    print("-------------------------------------------------------------\n")
    print(f"You answered {correct_count} out of 5, Your Score is {score}\n")
    print("-------------------------------------------------------------")


python_trivia_game()
