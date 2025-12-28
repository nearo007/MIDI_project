import mido
import time
import chord_progressions as prog

def get_output_names():
    ports = mido.get_output_names()
    print(ports)
    return ports

def get_output_port():
    for o in get_output_names():
        if o.find('MIDI') != -1:
            return o
        
def get_virtual_output_port():
    for o in get_output_names():
        if o.find('virtual') != -1:
            return o

def get_input_data():
    with mido.open_input() as port:
        while True:
            for message in  port:
                print(message)
                
def get_interval_speed(bpm, time_signature=1):
    bps = 60 / bpm
    return bps / time_signature


def play_output(outport, chord_progression, interval_speed, staccato_factor=0.5):
    note_duration = interval_speed * staccato_factor
    silence_duration = interval_speed - note_duration
    
    while True:
        for chord in chord_progression:
            for note in chord:
                outport.send(note)
            
            time.sleep(note_duration)
            
            for note in chord:
                for note in chord:
                    outport.send(mido.Message('note_off', note=note.note, velocity=0, channel=note.channel))
            
            time.sleep(silence_duration)

bpm = 120
interval_speed = get_interval_speed(bpm, 1)

# output_port = mido.open_output(get_virtual_output_port())
output_port = mido.open_output(get_output_port())

play_output(output_port, prog.c_blues_1, interval_speed, 0.5)