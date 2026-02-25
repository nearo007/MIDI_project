from flask import Flask, render_template
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Application:
    def __init__(self):
        self.app = Flask(__name__, root_path=str(BASE_DIR), template_folder='templates')

        @self.app.get("/")
        def index():
            name = "Everybody is,"
            surname = "Looking at me."
            
            context = {'name': name, 'surname': surname}
            return render_template("index.html", context=context)
        
        @self.app.get("/new")
        def new():
            name = "huh"
            return render_template("index.html", name=name)
    
    # def run(self, debug=False):
    #     self.app.run(debug=True)
        
def run():
    webapp = Application()
    webapp.app.run(debug=True)
    
if __name__ == '__main__':
    run()