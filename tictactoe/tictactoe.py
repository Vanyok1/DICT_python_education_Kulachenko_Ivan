def create_matrix():
    """Create initial TicTacToe game board

    Returns:
    list: 3x3 matrix with all cells set to underscore character
    """
    cells = "_________"
    return [
        [cells[0], cells[1], cells[2]],
        [cells[3], cells[4], cells[5]],
        [cells[6], cells[7], cells[8]]
    ]

def print_matrix(matrix):
    """Display the current game board

    Parameters:
    matrix (list): 3x3 matrix representing the current game state
    """
    print("---------")
    for row in matrix:
        print("|", row[0], row[1], row[2], "|")
    print("---------")

def check_winner(matrix):
    """Determine the status of the current game.

    Parameters:
        matrix (list): 3x3 matrix containing "X", "0", or "_" characters.

    Returns:
        str: One of the following status messages:
            - "Impossible": Invalid game state.
            - "X wins": Player X has won.
            - "0 wins": Player 0 has won.
            - "Game not finished": There are empty cells and no winner.
            - "Draw": Board is full with no winner.
    """
    flat = [c for row in matrix for c in row]

    x_count = flat.count("X")
    o_count = flat.count("0")
    empty = flat.count("_")

    lines = []

    for i in range(3):
        lines.append("".join(matrix[i]))

    for i in range(3):
        lines.append(matrix[0][i] + matrix[1][i] + matrix[2][i])

    lines.append(matrix[0][0] + matrix[1][1] + matrix[2][2])
    lines.append(matrix[0][2] + matrix[1][1] + matrix[2][0])

    x_win = "XXX" in lines
    o_win = "000" in lines

    if abs(x_count - o_count) >= 2 or (x_win and o_win):
        return "Impossible"

    if x_win:
        return "X wins"
    if o_win:
        return "0 wins"
    if empty > 0:
        return "Game not finished"

    return "Draw"

def player_move(matrix, turn):
    """Process a players move

    Parameters:
    matrix (list): 3x3 matrix representing the current game state
    turn (str): Current players symbol ("X" or "0")
    """
    while True:
        coords = input("Enter the coordinates: ").split()
        if not (len(coords) == 2 and coords[0].isdigit() and coords[1].isdigit()):
            print("You should enter numbers!")
            continue
        x, y = map(int, coords)
        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        if matrix[x - 1][y - 1] != "_":
            print("This cell is occupied! Choose another one!")
            continue
        matrix[x - 1][y - 1] = turn
        break

def main():
    """Main game loop for Tic-Tac-Toe

    Initializes and controls the flow of the Tic-Tac-Toe game. Creates the
    initial board, displays it, and alternates player turns until the game
    reaches a conclusion (win, draw, or impossible state).
    """
    matrix = create_matrix()
    print_matrix(matrix)
    turn = "X"

    while True:
        player_move(matrix, turn)
        print_matrix(matrix)
        result = check_winner(matrix)
        if result != "Game not finished":
            print(result)
            break
        turn = "0" if turn == "X" else "X"

if __name__ == "__main__":
    main()