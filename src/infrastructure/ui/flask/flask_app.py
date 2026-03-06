import os
from flask import Flask, render_template, jsonify
from src.infrastructure.ui.flask.controllers.player_controller import player_service_bp
from src.infrastructure.ui.flask.player_service import player_service

player_service.play_sequence([[60]])

class Application:
    def __init__(self):
        self.app = Flask(__name__, template_folder='view/templates')
        self.app.register_blueprint(player_service_bp)
    
    def run(self, debug=False):
        self.app.run(debug=True)
        
def run():
    webapp = Application()
    webapp.app.run(debug=True)
    
if __name__ == '__main__':
    run()