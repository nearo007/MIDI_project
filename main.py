import mido
import time
import notes as key

# mensagem = mido.Message('note_on')
# print(mensagem.bytes())



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
                
def get_interval_speed(bpm, time_signature=2):
    bps = 60 / bpm
    return bps / time_signature


def play_output(outport, chord_progression, interval_speed):
    while True:
        for chord in chord_progression:
            for note in chord:
                outport.send(note)
            
            time.sleep(interval_speed)
            
            for note in chord:
                outport.send(mido.Message('note_off', note.note))


# chord_progression = [[a3], [c3, e3], [e2], [c3, a3]]
chord_progression = [[key.c3], [key.d_sharp3, key.g3], [key.a_sharp3], [key.d3, key.f3], [key.g_sharp2], [key.c3, key.d_sharp3], [key.g2], [key.b3, key.d3]]

bpm = 100
interval_speed = get_interval_speed(bpm, 1)

output_port = mido.open_output(get_output_port())

play_output(output_port, chord_progression, interval_speed)
get_output_port()