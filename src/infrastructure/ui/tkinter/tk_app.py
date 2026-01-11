import tkinter as tk
from tkinter import ttk
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

def window_play():
    print(adapter.get_current_port())
    player.play_sequence(sequence, interval_speed=interval_speed, staccato=staccato)

def window_set_outport():
    adapter.set_outport(var_string.get())
    
# tkinter
root = tk.Tk()
root.geometry("1280x720")
frame = ttk.Frame(root, padding=10)

frame.grid()

ttk.Label(frame, text='MIDI Toolbox').grid(column=0, row=0)

try:
    default_opt = ports[0]
    var_string = tk.StringVar(value=default_opt)
    ttk.OptionMenu(frame, var_string, default_opt, *ports).grid(column=0, row=1)
except Exception as e:
    print(e)

ttk.Button(frame, text='Set Output Port', command=window_set_outport).grid(column=0, row=1)

ttk.Button(frame, text='Play scale', command=window_play).grid(column=0, row=2)
ttk.Button(frame, text='Let me out', command=root.destroy).grid(column=0, row=3)

def run():
    root.mainloop()