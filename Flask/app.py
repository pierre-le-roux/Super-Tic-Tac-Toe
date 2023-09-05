from flask import Flask, jsonify, request, render_template
from super_tic_tac_toe import SuperTicTacToe

app = Flask(__name__)
game = SuperTicTacToe()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/move", methods=["POST"])
def make_move_endpoint():
    data = request.json
    move = (
        int(data["mainRow"]),
        int(data["mainCol"]),
        int(data["miniRow"]),
        int(data["miniCol"]),
    )

    move_result = game.make_move(move)
    print(f"Result from make_move: {move_result}")

    valid_move = False if move_result is False else True

    print(f"Result from valid_move: {valid_move}")
    next_move, winning_combination = game.get_game_state()

    if valid_move:
        result = {
            "gameOver": game.game_over,
            "winner": game.winner,
            "currentPlayer": game.current_player,
            "board": game.board,
            "nextMove": next_move,
            "winningCombination": [
                {"mainRow": i, "mainCol": j} for i, j in winning_combination
            ],
            "miniGameWon": move_result["miniGameWon"]
            if not isinstance(move_result, bool)
            else False,
            "miniGameWinner": move_result["miniGameWinner"]
            if not isinstance(move_result, bool)
            else None,
            "miniGamePosition": move_result["miniGamePosition"]
            if not isinstance(move_result, bool)
            else None,
        }
        print(result)
        return jsonify(result), 200
    else:
        return jsonify({"error": "Invalid move"}), 400



@app.route("/restart", methods=["POST"])
def restart_game_endpoint():
    game.reset_game()
    return jsonify({"message": "Game restarted successfully!"}), 200


if __name__ == "__main__":
    app.run(debug=True)
