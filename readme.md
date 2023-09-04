# Super Tic Tac Toe

Welcome to Super Tic Tac Toe, a twist on the classic Tic Tac Toe game. Instead of playing on just one 3x3 board, each cell of the main board is a mini 3x3 Tic Tac Toe board itself!

## Rules

1. **Starting**: The first player (X) can make a move in any cell of any mini board.
2. **Subsequent Moves**: The next move must be made within the mini board corresponding to the cell of the last move. For example, if Player X makes a move in the middle cell of a mini board, Player O's next move must be made somewhere within the middle mini board of the main board.
3. **Winning**: To win a mini board, a player must get three of their symbols in a row, column, or diagonal. To win the main game, a player must win three mini boards in a row, column, or diagonal.

```
Main Board:
+-------+-------+-------+
|  1,1  |  1,2  |  1,3  |
+-------+-------+-------+
|  2,1  |  2,2  |  2,3  |
+-------+-------+-------+
|  3,1  |  3,2  |  3,3  |
+-------+-------+-------+

Each cell (like 1,1) is itself a mini 3x3 board:
+---+---+---+
| X | O | X |
+---+---+---+
| O | X | O |
+---+---+---+
| X |   | O |
+---+---+---+
```

## Code Structure

The codebase is divided into three main files:

- `main.py`: This file runs the game.
- `super_tic_tac_toe.py`: Houses the main `SuperTicTacToe` class responsible for the game logic and GUI.
- `utility.py`: Contains helper functions that the main game class uses.

## How to Run

1. Ensure you have Python installed.
2. Install the necessary package:
   ```
   pip install tkinter
   ```
3. Navigate to the directory containing the game files and run:
   ```
   python main.py
   ```

Enjoy the game!
---