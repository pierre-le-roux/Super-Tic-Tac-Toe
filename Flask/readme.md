# Super Tic Tac Toe

Welcome to Super Tic Tac Toe! This game builds upon the classic Tic Tac Toe, adding another layer of strategy and challenge.

## Project Structure

- `index.html`: Contains the main structure of the game board.
- `styles.css`: Holds all the styling elements of the game, ensuring the board and cells are visually appealing and responsive.
- `script.js`: Manages the game's front-end logic, handling player interactions, valid move highlights, and more.
- `app.py`: The main server-side script powered by Flask. It communicates with the front-end, processes game logic, and updates game states.
- `super_tic_tac_toe.py`: Houses the core game logic for Super Tic Tac Toe.
- `utility.py`: Contains helper functions to aid the game logic.

## How to Play

1. **Starting a Game**: When the game starts, either player can make the first move in any mini-game.
2. **Game Flow**: After the first move, the next player must play in the mini-game corresponding to the cell picked in the previous move. For instance, if Player 1 picks the center cell of a mini-game, Player 2 must play in the center mini-game.
3. **Winning a Mini-Game**: To win a mini-game, a player must get three of their marks in a row, either horizontally, vertically, or diagonally.
4. **Winning the Main Game**: To win the main game, a player must win three mini-games in a row, again either horizontally, vertically, or diagonally.
5. **Game Over**: Once the main game is won, no further moves can be made unless the game is restarted.
6. **Restarting the Game**: At any point, players can restart the game by clicking the 'Restart' button.

## Features

- **Responsive Design**: The game board adjusts to fit the screen, ensuring a great gaming experience.
- **Visual Highlights**: Cells and mini-games that are valid moves are highlighted to guide the players.
- **End Game**: Once the game is over, further moves are disabled, ensuring the game state remains consistent.
- **Winner Tiles**: When a mini-game is won, the entire mini-game transforms into a large tile with the winner's mark, either 'X' or 'O'.

## Known Issues

None as of the latest update.

## Future Enhancements

- Implement a multiplayer mode for remote play.
- Add a timer for each player's turn to increase the challenge.
- Some short tutorial or explanation of how the game works.