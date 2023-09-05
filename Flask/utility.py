def get_next_board(last_move, main_board_state):
    """
    Get the next board based on the last move.

    Args:
    - last_move (tuple): A tuple of the form (main_row, main_col, mini_row, mini_col)
    - main_board_state (list): A 3x3 list indicating which mini boards have been won.

    Returns:
    - next_board (tuple): A tuple of the form (main_row, main_col)
    """

    # Check if the game just started
    if last_move is None:
        return None

    # Get the previous move indicating the next mini-game location
    _, _, mini_row, mini_col = last_move
    
    print("main board state:", main_board_state)
    print(f"last move: {last_move}")
    print(f"main board state: {main_board_state[mini_row][mini_col] == ''}\n")

    # If the determined mini board is already won, return None, indicating player can choose any board.
    if main_board_state[mini_row][mini_col] != "":
        return None

    return (mini_row, mini_col)


def check_mini_win(mini_board):
    """
    Check if a player has won the mini tic-tac-toe game.

    Args:
    - mini_board (list): A 3x3 matrix representing the mini tic-tac-toe board.

    Returns:
    - str: "X" if X has won, "O" if O has won, and "" if no one has won.
    """

    # Check rows and columns
    for i in range(3):
        if (
            mini_board[i][0] == mini_board[i][1] == mini_board[i][2]
            and mini_board[i][0] != ""
        ):
            return mini_board[i][0]
        if (
            mini_board[0][i] == mini_board[1][i] == mini_board[2][i]
            and mini_board[0][i] != ""
        ):
            return mini_board[0][i]

    # Check diagonals
    if (
        mini_board[0][0] == mini_board[1][1] == mini_board[2][2]
        and mini_board[0][0] != ""
    ):
        return mini_board[0][0]
    if (
        mini_board[0][2] == mini_board[1][1] == mini_board[2][0]
        and mini_board[0][2] != ""
    ):
        return mini_board[0][2]

    return ""


def check_mini_draw(mini_board):
    """
    Check if the mini tic-tac-toe game has resulted in a draw.

    Args:
    - mini_board (list): A 3x3 matrix representing the mini tic-tac-toe board.

    Returns:
    - bool: True if the game is a draw, False otherwise.
    """

    # Check if all positions are occupied
    all_occupied = all(cell != "" for row in mini_board for cell in row)

    return all_occupied and not check_mini_win(mini_board)



def check_main_win(main_board_state):
    """
    Check if a player has won the main tic-tac-toe game.

    Args:
    - main_board_state (list): A 3x3 matrix indicating which mini boards have been won.

    Returns:
    - str: "X" if X has won, "O" if O has won, and "" if no one has won.
    """

    # Check rows and columns
    for i in range(3):
        if (
            main_board_state[i][0] == main_board_state[i][1] == main_board_state[i][2]
            and main_board_state[i][0] != ""
        ):
            return main_board_state[i][0], [(i, 0), (i, 1), (i, 2)]
        if (
            main_board_state[0][i] == main_board_state[1][i] == main_board_state[2][i]
            and main_board_state[0][i] != ""
        ):
            return main_board_state[0][i], [(0, i), (1, i), (2, i)]

    # Check diagonals
    if (
        main_board_state[0][0] == main_board_state[1][1] == main_board_state[2][2]
        and main_board_state[0][0] != ""
    ):
        return main_board_state[0][0], [(0, 0), (1, 1), (2, 2)]
    if (
        main_board_state[0][2] == main_board_state[1][1] == main_board_state[2][0]
        and main_board_state[0][2] != ""
    ):
        return main_board_state[0][2], [(0, 2), (1, 1), (2, 0)]

    return "", []
