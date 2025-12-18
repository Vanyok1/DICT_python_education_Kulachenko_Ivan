import random

def get_secret_word():
    """Return a randomly chosen secret word.

    Returns:
        str: Randomly selected word.
    """
    words = ['python', 'java', 'javascript', 'php']
    return random.choice(words)

def initialize_display(secret_word):
    """Return a masked display for the secret word.

    Parameters:
        secret_word (str): Word to hide.

    Returns:
        str: String of hyphens.
    """
    return "-" * len(secret_word)

def validate_input(letter, guessed_letters):
    """Validate player's input letter.

    Parameters:
        letter (str): Input character.
        guessed_letters (set): Previously guessed letters.

    Returns:
        tuple: (bool, str) validity flag and message.
    """
    if len(letter) != 1:
        return False, "You should input a single letter"
    if not letter.isalpha() or not letter.islower():
        return False, "Please enter a lowercase English letter"
    if letter in guessed_letters:
        return False, "You've already guessed this letter"
    return True, ""

def update_display(secret_word, display, letter):
    """Update display after guessing a letter.

    Parameters:
        secret_word (str): Actual word.
        display (str): Current masked display.
        letter (str): Guessed character.

    Returns:
        tuple: (str, bool) updated display and improvement flag.
    """
    new_display = ""
    improved = False

    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            new_display += letter
            improved = True
        else:
            new_display += display[i]

    return new_display, improved

def play_game():
    """Run the full Hangman game loop.

    Starts a new game, handles user input, updates attempts,
    checks win/loss conditions, and prints game messages.

    Returns:
        None
    """
    secret_word = get_secret_word()
    display = initialize_display(secret_word)
    attempts = 8
    guessed_letters = set()

    print(display)

    while attempts > 0 and display != secret_word:
        letter = input("Input a letter: ")

        valid, message = validate_input(letter, guessed_letters)
        if not valid:
            print(message)
            print(display)
            continue

        guessed_letters.add(letter)

        if letter in secret_word:
            display, improved = update_display(secret_word, display, letter)
            if not improved:
                print("No improvements")
                attempts -= 1
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1

        print(display)

    if display == secret_word:
        print(f"You guessed the word {secret_word}!")
        print("You survived!")
    else:
        print("You lost!")

def main():
    """Start the program and handle the main menu loop.

    Prompts the user to start a new game or exit.

    Returns:
        None
    """
    print("HANGMAN")
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ')
        if choice == "play":
            play_game()
        elif choice == "exit":
            break

main()