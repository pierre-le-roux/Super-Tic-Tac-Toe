document.addEventListener("DOMContentLoaded", function () {
    const cells = document.querySelectorAll('.mini-cell');
    const statusBar = document.getElementById('status-bar');
    const restartBtn = document.getElementById('restart-btn');
    let gameOver = false;

    cells.forEach(cell => {
        cell.addEventListener('click', handleMove);
    });


    restartBtn.addEventListener('click', function () {
        fetch('/restart', {
            method: 'POST'
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                gameOver = false;  // Reset the gameOver state
                
                // Clear all cells and reset the status bar
                cells.forEach(cell => {
                    cell.textContent = "";
                });
                statusBar.textContent = "Player X's turn";
    
                // Remove any highlights and reset all main cells
                const mainCells = document.querySelectorAll('.main-cell');
                mainCells.forEach(cell => {
                    cell.classList.remove('next-move', 'winner', 'x', 'o');
                    const mainRow = cell.dataset.mainRow;
                    const mainCol = cell.dataset.mainCol;
                    updateMiniGameWinner(mainRow, mainCol, null);  // Reset to original mini-game layout
                });
            }
        });
    });
    


    function updateMiniGameWinner(mainRow, mainCol, winner) {
        const mainCell = document.querySelector(`.main-cell[data-main-row="${mainRow}"][data-main-col="${mainCol}"]`);
    
        if (winner) {
            // Remove all mini-cells from the main-cell if there's a winner
            while (mainCell.firstChild) {
                mainCell.removeChild(mainCell.firstChild);
            }
    
            // Add a big tile with the winner's symbol
            const winnerTile = document.createElement('div');
            winnerTile.classList.add('winner-tile', winner.toLowerCase());
            winnerTile.textContent = winner;
            mainCell.appendChild(winnerTile);
        } else {
            // If no winner, recreate the mini-cells for the mini-game
            mainCell.innerHTML = "";
            for (let i = 0; i < 3; i++) {
                const miniRow = document.createElement('div');
                miniRow.classList.add('mini-row');
                for (let j = 0; j < 3; j++) {
                    const miniCell = document.createElement('button');
                    miniCell.classList.add('mini-cell');
                    miniCell.dataset.mainRow = mainRow;
                    miniCell.dataset.mainCol = mainCol;
                    miniCell.dataset.miniRow = i;
                    miniCell.dataset.miniCol = j;
                    miniCell.addEventListener('click', handleMove);
                    miniRow.appendChild(miniCell);
                }
                mainCell.appendChild(miniRow);
            }
        }
    }
    


    function handleMove(event) {
        if (gameOver) return;
        const cell = event.target;
        const mainCell = cell.closest('.main-cell');

        const isInitialMove = document.querySelectorAll('.main-cell.next-move').length === 0;

        // Check if the cell is already occupied
        if (cell.textContent) {
            return;  // Exit the function without processing the move
        }
    
        // Check if the clicked cell is within the highlighted (valid) mini-game
        if (!isInitialMove && !mainCell.classList.contains('next-move')) {
            return; // If not, exit the function early
        }
    
        const moveData = {
            mainRow: cell.dataset.mainRow,
            mainCol: cell.dataset.mainCol,
            miniRow: cell.dataset.miniRow,
            miniCol: cell.dataset.miniCol
        };
    
        fetch('/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(moveData)
        })
            .then(response => response.json())
            .then(data => {
                gameOver = data.gameOver;  // Update the gameOver state based on the server response

                if (data.error) {
                    alert(data.error);
                } else {
                    cell.textContent = data.currentPlayer === "X" ? "O" : "X";
                    // Check if a mini-game has been won
                    if (data.miniGameWon) {
                        updateMiniGameWinner(data.miniGamePosition[0], data.miniGamePosition[1], data.miniGameWinner);
                    }
    
                    if (data.gameOver) {
                        statusBar.textContent = `Player ${data.winner} has won!`;
                        highlightWinningCombination(data.winningCombination);
                    } else {
                        statusBar.textContent = `Player ${data.currentPlayer}'s turn`;
                        highlightNextMove(data.nextMove);
                    }
                    // Check if a mini-game has been won
                    if (data.miniGameWinner) {
                        updateMiniGameWinner(data.miniGameWinner.mainRow, data.miniGameWinner.mainCol, data.miniGameWinner.winner);
                    }
                }
            });
    }
    

    function highlightNextMove(nextMove) {
        // Remove the previous highlights
        const highlighted = document.querySelectorAll('.main-cell.next-move');
        highlighted.forEach(cell => {
            cell.classList.remove('next-move');
        });
    
        // If nextMove is not provided or contains null values, highlight all available spaces
        if (!nextMove || (nextMove[0] === null && nextMove[1] === null)) {
            // Highlight available mini-games
            const availableCells = document.querySelectorAll('.main-cell:not(.winner-tile):not(.x):not(.o)');
            availableCells.forEach(cell => {
                if (!cell.querySelector('.winner-tile')) {
                    cell.classList.add('next-move');
                }
            });
            return;
        }
    
        // Else, highlight the specific next move
        const mainRow = nextMove[0];
        const mainCol = nextMove[1];
        const mainCell = document.querySelector(`.main-cell[data-main-row="${mainRow}"][data-main-col="${mainCol}"]`);
        
        // Check if the main cell already has a winner tile before highlighting
        if (mainCell.querySelector('.winner-tile')) {
            return;
        }
        
        mainCell.classList.add('next-move');
    }
    

    function highlightWinningCombination(winningCombination) {
        // Remove the previous winner highlights
        const winners = document.querySelectorAll('.main-cell.winner');
        winners.forEach(cell => {
            cell.classList.remove('winner');
        });
        if (winningCombination) {
            winningCombination.forEach(({ mainRow, mainCol }) => {
                const mainCell = document.querySelector(`.main-cell[data-main-row="${mainRow}"][data-main-col="${mainCol}"]`);
                mainCell.classList.add('winner');
            });
        }
        // Remove highlight from all mini-games at game end
        const highlighted = document.querySelectorAll('.main-cell.next-move');
        highlighted.forEach(cell => {
            cell.classList.remove('next-move');
        });
    }

});