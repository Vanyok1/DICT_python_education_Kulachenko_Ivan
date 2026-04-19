import random

def get_level():
    """Get difficulty level from user.

    Prompts the user to choose a difficulty level (1 or 2).
    Repeats until correct input is provided.

    Returns:
        int: selected level (1 or 2)
    """
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        choice = input("> ")
        if choice in ["1", "2"]:
            return int(choice)
        else:
            print("Incorrect format.")

def generate_task(level):
    """Generate arithmetic task based on level.

    Parameters:
        level (int): difficulty level (1 or 2)

    Returns:
        tuple: (question (str), correct_answer (int))
    """
    if level == 1:
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op = random.choice(['+', '-', '*'])
        question = f"{a} {op} {b}"
        if op == '+':
            answer = a + b
        elif op == '-':
            answer = a - b
        else:
            answer = a * b
    else:
        a = random.randint(11, 29)
        question = f"{a}"
        answer = a * a
    return question, answer

def get_answer():
    """Get numeric answer from user.

    Repeats input request until user enters a valid integer.

    Returns:
        int: user answer
    """
    while True:
        user_input = input("> ")
        try:
            return int(user_input)
        except:
            print("Incorrect format.")

def save_result(score, level):
    """Save test result to file.

    Asks user whether to save the result. If yes, asks for name
    and writes result to 'results.txt'.

    Parameters:
        score (int): number of correct answers
        level (int): selected difficulty level

    Returns:
        None
    """
    print("Would you like to save your result to the file? Enter yes or no.")
    choice = input("> ")

    if choice.lower() in ["yes", "y"]:
        print("What is your name?")
        name = input("> ")

        if level == 1:
            desc = "simple operations with numbers 2-9"
        else:
            desc = "integral squares of 11-29"

        with open("results.txt", "a") as file:
            file.write(f"{name}: {score}/5 in level {level} ({desc}).\n")

        print('The results are saved in "results.txt".')

level = get_level()
score = 0

for _ in range(5):
    question, correct = generate_task(level)
    print(question)

    answer = get_answer()

    if answer == correct:
        print("Right!")
        score += 1
    else:
        print("Wrong!")
print(f"Your mark is {score}/5.")
save_result(score, level)