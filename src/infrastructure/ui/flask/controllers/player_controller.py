from flask import Blueprint, jsonify, render_template, request
from src.infrastructure.ui.flask.player_service import player_service

player_service_bp = Blueprint('player_service_bp', __name__)

@player_service_bp.route('/')
def index():
    name = "Everbody is,"
    surname = "Looking at me."
    
    return render_template('index.html')

@player_service_bp.route("/play", methods=['POST'])
def play():
    key_num = request.form.get("key_num")
    print(key_num)
    try:
        key_num = int(key_num)
        player_service.play_async([[key_num]])
    except Exception as e:
        print(f"Oh no!\n{e}")
    
    return "", 204

@player_service_bp.route("/chord-lab", methods=['GET'])
def chord_lab():
    return render_template("index.html")