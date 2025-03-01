from flask import Blueprint, render_template, request
from .game_logic import Character, Enemy

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        player_name = request.form.get('player_name')
        class_type = request.form.get('class_type')
        player = Character(player_name, class_type)
        return render_template('game.html', player=player)
    return render_template('game.html')