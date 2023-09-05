from utility import get_next_board, check_mini_win, check_main_win, check_mini_draw


class SuperTicTacToe:
    def __init__(self):
        self.game_over = False
        self.board = [
            [[["" for _ in range(3)] for _ in range(3)] for _ in range(3)]
            for _ in range(3)
        ]
        self.main_board_state = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.last_move = None
        self.winner = None  # new attribute to keep track of the winner
        self.winning_combination = []

    def make_move(self, move):
        print(f"Making move: {move}")  # Log the move being made
        mini_game_won = False
        mini_game_winner = None
        mini_game_position = None

        if self.is_valid_move(self.board, self.main_board_state, self.last_move, move):
            i, j, x, y = move
            self.board[i][j][x][y] = self.current_player

            # Check if mini game is won
            winner = check_mini_win(self.board[i][j])
            if winner:
                mini_game_won = True
                mini_game_winner = winner
                mini_game_position = (i, j)
                self.main_board_state[i][j] = winner
                # Set all cells of the mini-game to the winner
                for x in range(3):
                    for y in range(3):
                        self.board[i][j][x][y] = winner

                # Check if main game is won
                winner, self.winning_combination = check_main_win(self.main_board_state)
                if winner:
                    self.game_over = True
                    self.winner = winner
                else:
                    self.winning_combination = []

            # If not won, then check if mini game is a draw
            elif check_mini_draw(self.board[i][j]):
                # Reset the mini-game board
                for x in range(3):
                    for y in range(3):
                        self.board[i][j][x][y] = ""

            self.last_move = move
            # Switch to the next player
            self.current_player = "O" if self.current_player == "X" else "X"

        return {
            "board": self.board,
            "currentPlayer": self.current_player,
            "lastMove": self.last_move,
            "miniGameWon": mini_game_won,
            "miniGameWinner": mini_game_winner,
            "miniGamePosition": mini_game_position,
            "mainBoardState": self.main_board_state,
        }

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
        print(f"Last move: {last_move}")  # Log the last move
        print(f"Current move: {current_move}")  # Log the current move

        next_board = get_next_board(last_move, main_board_state)
        print(f"Next board: {next_board}")  # Log the next board

        # If next board is None, player can choose any mini board.
        if not next_board:
            main_row, main_col, mini_row, mini_col = current_move
            # Check if the chosen cell within the mini board is empty.
            if board[main_row][main_col][mini_row][mini_col] == "":
                # print("Valid move because it's the first move and the chosen cell is empty.")
                return True
            else:
                # print("Invalid move because the chosen cell is not empty.")
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

    def get_game_state(self):
        next_board = get_next_board(self.last_move, self.main_board_state)
        return next_board, self.winning_combination

    def reset_game(self):
        self.game_over = False
        self.board = [
            [[["" for _ in range(3)] for _ in range(3)] for _ in range(3)]
            for _ in range(3)
        ]
        self.main_board_state = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.last_move = None
        self.winner = None
        self.winning_combination = []
