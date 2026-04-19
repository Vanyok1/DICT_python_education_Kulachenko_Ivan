import random

def load_rating(name):
    """
    Load user rating from file rating.txt.

    Parameters:
    name (str): user name

    Returns:
    int: rating value (0 if not found)
    """
    rating = 0
    try:
        with open("rating.txt", "r") as file:
            for line in file:
                user, score = line.split()
                if user == name:
                    rating = int(score)
    except FileNotFoundError:
        pass
    return rating

def get_wins(user_choice, options):
    """
    Get options that beat user_choice based on cyclic rule.

    Parameters:
    user_choice (str): selected option
    options (list): list of all options

    Returns:
    list: options that user loses to (half circle)
    """
    idx = options.index(user_choice)
    half = len(options) // 2
    return [
        options[(idx + i) % len(options)]
        for i in range(1, half + 1)
    ]

name = input("Enter your name: ")
print(f"Hello, {name}")

rating = load_rating(name)

options_input = input()

if options_input == "":
    options = ["rock", "paper", "scissors"]
else:
    options = options_input.split(",")

print("Okay, let's start")

while True:
    user = input()
    if user == "!exit":
        print("Bye!")
        break
    if user == "!rating":
        print(f"Your rating: {rating}")
        continue
    if user not in options:
        print("Invalid input")
        continue

    computer = random.choice(options)
    if user == computer:
        print(f"There is a draw ({computer})")
        rating += 50
    else:
        wins = get_wins(user, options)
        if computer in wins:
            print(f"Sorry, but the computer chose {computer}")
        else:
            print(f"Well done. The computer chose {computer} and failed")
            rating += 100