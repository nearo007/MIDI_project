# from src.infrastructure.ui.cli.cli_app import run as run_cli_app
# from src.infrastructure.ui.tkinter.tk_app import run as run_window_app
from src.infrastructure.ui.flask.flask_app import run as run_webapp_app

import sys
sys.dont_write_bytecode = True

if __name__ == '__main__':
    run_webapp_app()