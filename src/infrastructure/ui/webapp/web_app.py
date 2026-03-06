from flask import Flask, render_template, jsonify
import os
from src.infrastructure.ui.webapp.controllers.play_controller import player_service_bp

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Application:
    def __init__(self):
        self.app = Flask(__name__, root_path=str(BASE_DIR), template_folder='view/templates')
        self.app.register_blueprint(player_service_bp)
    
    # def run(self, debug=False):
    #     self.app.run(debug=True)
        
def run():
    webapp = Application()
    webapp.app.run(debug=True)
    
if __name__ == '__main__':
    run()