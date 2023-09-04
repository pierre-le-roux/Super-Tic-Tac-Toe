import tkinter as tk
from tkinter import Button


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

    _, _, mini_row, mini_col = last_move

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


class SuperTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Tic Tac Toe")

        # Initialize game state
        self.game_over = False
        self.board = [
            [[["" for _ in range(3)] for _ in range(3)] for _ in range(3)]
            for _ in range(3)
        ]
        self.main_board_state = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.last_move = None
        self.buttons = [
            [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]
            for _ in range(3)
        ]

        # Create the GUI layout
        for i in range(3):
            for j in range(3):
                frame = tk.Frame(self.root, borderwidth=2, relief="groove")
                frame.grid(row=i, column=j, padx=5, pady=5)
                for x in range(3):
                    for y in range(3):
                        btn = Button(frame, text="", width=10, height=3)
                        btn.grid(row=x, column=y, padx=2, pady=2)
                        btn.bind("<Button-1>", self.on_click)
                        self.buttons[i][j][x][y] = btn

    def on_click(self, event):
        # If the game has ended, don't process further clicks
        if self.game_over:
            return
                
        self.reset_highlights()  # Clear previous highlights

        # Determine which button was clicked
        for i in range(3):
            for j in range(3):
                for x in range(3):
                    for y in range(3):
                        if self.buttons[i][j][x][y] == event.widget:
                            if self.is_valid_move(self.board, self.main_board_state, self.last_move, (i, j, x, y)):
                                self.update_game((i, j, x, y))
        # Now, only highlight next move if the game hasn't ended
        if not self.game_over:
            self.highlight_next_move()

    def update_game(self, move):
        i, j, x, y = move
        self.board[i][j][x][y] = self.current_player
        self.buttons[i][j][x][y]["text"] = self.current_player

        # Check if mini game is won
        winner = check_mini_win(self.board[i][j])
        if winner:
            self.main_board_state[i][j] = winner
            for a in range(3):
                for b in range(3):
                    self.buttons[i][j][a][b]["state"] = tk.DISABLED
                    self.buttons[i][j][a][b]["text"] = winner

        # Check if main game is won
        winner, winning_combination = check_main_win(self.main_board_state)
        if winner:
            self.disable_remaining_squares()
            self.highlight_winning_combination(winning_combination)
            self.display_winner_banner(winner)
            self.game_over = True

        self.last_move = move
        # Switch to the next player
        self.current_player = "O" if self.current_player == "X" else "X"

    def is_valid_move(self, board, main_board_state, last_move, current_move):
        """
        Check if the given move is valid.

        Args:
        - board (list): The current state of the board.
        - main_board_state (list): A 3x3 list indicating which mini boards have been won.
        - last_move (tuple): A tuple of the form (main_row, main_col, mini_row, mini_col) representing the last move made.
        - current_move (tuple): A tuple of the form (main_row, main_col, mini_row, mini_col) representing the current move.

        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        next_board = get_next_board(last_move, main_board_state)

        # If next board is None, player can choose any mini board.
        if not next_board:
            main_row, main_col, mini_row, mini_col = current_move
            # Check if the chosen cell within the mini board is empty.
            if board[main_row][main_col][mini_row][mini_col] == "":
                return True
            else:
                return False
        else:
            main_row, main_col, mini_row, mini_col = current_move
            # Check if the player is playing in the correct mini board and the chosen cell is empty.
            if (main_row, main_col) == next_board and board[main_row][main_col][
                mini_row
            ][mini_col] == "":
                return True
            else:
                return False

    def reset_highlights(self):
        for i in range(3):
            for j in range(3):
                frame = self.buttons[i][j][0][0].master
                frame.config(bg="white")  # Reset to default background

    def highlight_next_move(self):
        next_board = get_next_board(self.last_move, self.main_board_state)

        # If there's a specific next board
        if next_board:
            i, j = next_board
            frame = self.buttons[i][j][0][0].master
            frame.config(bg="yellow")  # Highlight specific mini-board
        else:
            # Highlight all available mini-boards
            for i in range(3):
                for j in range(3):
                    if self.main_board_state[i][j] == "":
                        frame = self.buttons[i][j][0][0].master
                        frame.config(bg="yellow")

    def highlight_winning_combination(self, winning_combination):
        for i, j in winning_combination:
            frame = self.buttons[i][j][0][0].master
            frame.config(bg="green")  # Highlight the winning mini-boards

    def disable_remaining_squares(self):
        for i in range(3):
            for j in range(3):
                for x in range(3):
                    for y in range(3):
                        if self.buttons[i][j][x][y]["text"] == "":
                            self.buttons[i][j][x][y]["state"] = tk.DISABLED

    def display_winner_banner(self, winner):
        banner = tk.Label(
            self.root,
            text=f"Congratulations Player {winner} won!",
            bg="red",
            fg="white",
            font=("Arial", 20),
        )
        banner.grid(row=3, column=0, columnspan=3)


# Create the main window
root = tk.Tk()
game = SuperTicTacToe(root)
root.mainloop()