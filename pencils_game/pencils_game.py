import random

players = ["John", "Jack"]

def get_pencils() -> int:
    """
    Ask the user how many pencils to use in the game.

    Returns:
    int: Number of pencils chosen by the user
    """
    print("How many pencils would you like to use:")
    while True:
        pencils = input()
        if not pencils.isdigit():
            print("The number of pencils should be numeric")
            continue
        pencils = int(pencils)
        if pencils <= 0:
            print("The number of pencils should be positive")
            continue
        return pencils

def choose_first_player() -> str:
    """
    Ask the user who will go first: John or Jack.

    Returns:
    str: Name of the first player
    """
    print(f"Who will be the first ({players[0]}, {players[1]}):")
    while True:
        current = input()
        if current not in players:
            print(f"Choose between '{players[0]}' and '{players[1]}'")
            continue
        return current

def player_move(pencils: int) -> int:
    """
    Process the move for the human player (John).

    Parameters:
    pencils (int): Number of pencils remaining

    Returns:
    int: Number of pencils taken by the player
    """
    while True:
        taken = input()
        if taken not in ("1", "2", "3"):
            print("Possible values: '1', '2' or '3'")
            continue
        taken = int(taken)
        if taken > pencils:
            print("Too many pencils were taken")
            continue
        return taken

def bot_move(pencils: int) -> int:
    """
    Process the move for the bot player (Jack) using an optimal strategy.

    Parameters:
    pencils (int): Number of pencils remaining

    Returns:
    int: Number of pencils taken by the bot
    """
    if pencils == 1:
        taken = 1
    elif pencils % 4 == 1:
        taken = random.randint(1, min(3, pencils))
    else:
        taken = (pencils - 1) % 4
    print(taken)
    return taken

def main():
    """
    Main function to run the pencil game.
    """
    pencils = get_pencils()
    current = choose_first_player()
    print("|" * pencils)

    while pencils > 0:
        print(f"{current}'s turn:")
        if current == "Jack":
            taken = bot_move(pencils)
        else:
            taken = player_move(pencils)

        pencils -= taken

        if pencils == 0:
            winner = players[0] if current == players[1] else players[1]
            print(f"{winner} won!")
            break

        print("|" * pencils)
        current = players[0] if current == players[1] else players[1]

if __name__ == "__main__":
    main()