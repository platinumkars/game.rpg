from flask import Blueprint, render_template, jsonify, request
from game_logic import Character, Enemy

# Create a Blueprint
game_bp = Blueprint('game', __name__)

@game_bp.route('/')
def index():
    return render_template('index.html')
    
@game_bp.route('/game')
def game():
    return render_template('game.html')
    
@game_bp.route('/api/create_character', methods=['POST'])
def create_character():
    data = request.json
    character = Character(data['name'], data['class_type'])
    return jsonify(character.__dict__)
