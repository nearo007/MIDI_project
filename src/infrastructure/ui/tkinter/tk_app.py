import threading
from .window import Window
from ...adapters.mido_adapter import MidoAdapter
from ....application.player_service import PlayerService
from ....domain.music_theory import get_scale_notes, to_playable_sequence
from ....domain.bpm import get_interval_speed

# mido
adapter = MidoAdapter()
adapter.pick_port()
player = PlayerService(adapter)
scale = get_scale_notes()
sequence = to_playable_sequence(scale)

ports = adapter.available_outports()
bpm = 120
interval_speed = get_interval_speed(bpm)
staccato = 0.5

playing = False
play_thread = None

def set_outport(port_name):
    sequence_stop()
    adapter.set_outport(port_name)
    
def sequence_start():
    global playing
    global play_thread
    
    if playing:
        return
    
    playing = True
    play_thread = threading.Thread(target=play_loop, daemon=True)
    play_thread.start()
    
def sequence_stop():
    global playing
    
    playing = False
    
def play_loop():
    global playing
    
    while playing:
        player.play_sequence(sequence, interval_speed, staccato)

# tkinter
window = Window()

window.add_label(text="MIDI Toolbox", grid=[0,0])

window.add_option_menu(options=ports, grid=[0, 1])
    
window.add_button(text="Set Output Port", command=lambda: set_outport(port_name=window.display_string.get()), grid=[1, 1])
window.add_button(text="Play scale", command=sequence_start, grid=[0, 2])
window.add_button(text="Stop", command=sequence_stop, grid=[1, 2])
window.add_button(text="Let me out", command=window.root.destroy, grid=[0, 3])

def run():
    window.run()
    
if __name__ == '__main__':
    run()