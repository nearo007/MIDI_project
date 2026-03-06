from flask import Blueprint, jsonify, render_template
from src.infrastructure.ui.webapp.player_service import player_service

player_service_bp = Blueprint('player_service_bp', __name__)

@player_service_bp.route("/")
def index():
    name = "Everybody is,"
    surname = "Looking at me."
    
    context = {'name': name, 'surname': surname}
    return render_template("index.html", context=context)

@player_service_bp.route("/new")
def new():
    name = "huh"
    return render_template("index.html", name=name)

@player_service_bp.route('/play')
def play():
    return jsonify({"status": "ok"})