from flask import Blueprint, jsonify, render_template, request, redirect
from src.infrastructure.ui.flask.instance import player_service
from src.domain.music_theory import get_scale_notes, get_chord

player_service_bp = Blueprint('player_service_bp', __name__)

@player_service_bp.route('/')
def index():    
    return redirect('/piano')

@player_service_bp.route('/piano')
def piano():
    return render_template("piano.html")

@player_service_bp.route("/play", methods=['POST'])
def play():
    key_num = request.form.get("key_num")
    try:
        key_num = int(key_num)
        player_service.play_sequence([[key_num]])
    except Exception as e:
        print(f"Oh no!\n{e}")
    
    return "", 204

@player_service_bp.route("/chord-lab", methods=['GET'])
def chord_lab():
    return render_template("chord-lab.html")

@player_service_bp.route("/chord-lab/start-progression", methods=['POST'])
def start_progression():
    player_service.set_bpm(bpm=80) #TODO hard coded
    player_service.set_staccato(staccato_value=1) #TODO hard coded
    
    progression = request.json['progression']
    
    playable_progression = []
        
    for chord in progression:
        chromatic_scale = get_scale_notes(mode=3, key=chord[0], octave=chord[1])
        playable_progression.append(get_chord(scale=chromatic_scale, tonality=chord[2], seventh=chord[3]))
    
    player_service.loop_sequence(sequence=playable_progression)
    return "", 204

@player_service_bp.route("/chord-lab/stop-progression", methods=['POST'])
def stop_progression():
    player_service.stop_loop()
    return "", 204