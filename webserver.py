from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/sudoku', methods=["GET", "POST"])
def sudoku():
    return render_template('sudoku.html')

@app.route('/sudoku_game', methods=["GET", "POST"])
def sudoku_game():
    return render_template('sudoku_game.html', mode=request.args.get("diff"))

app.run(host="0.0.0.0", port=80)