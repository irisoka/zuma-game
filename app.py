from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

game_state = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shoot_ball/<color>')
def shoot_ball(color):
    global game_state
    ball = {'color': color}
    game_state.append(ball)
    return f"Shooting a {color} ball !"


if __name__ == '__main__':
    app.run(debug=True)