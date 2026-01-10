from tkinter import *
from tkinter import ttk
from ...adapters.mido_adapter import MidoAdapter
from ....application.player_service import PlayerService
from ....domain.music_theory import get_scale_notes, to_playable_sequence
from ....domain.bpm import get_interval_speed
# mido
adapter = MidoAdapter()
adapter.set_outport('CASIO USB-MIDI 1')
player = PlayerService(adapter)
scale = get_scale_notes()
sequence = to_playable_sequence(scale)

bpm = 120
interval_speed = get_interval_speed(bpm)
staccato = 0.5

def window_play():
    player.play_sequence(sequence, interval_speed=interval_speed, staccato=staccato)

# tkinter
root = Tk()
frame = ttk.Frame(root, padding=10)

frame.grid()

ttk.Label(frame, text='MIDI Toolbox').grid(column=0, row=0)
ttk.Button(frame, text='Play scale', command=window_play).grid(column=0, row=1)
ttk.Button(frame, text='Let me out', command=root.destroy).grid(column=0, row=2)

def run():
    root.mainloop()