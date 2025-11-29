import mido
import time
# mensagem = mido.Message('note_on')
# print(mensagem.bytes())

outport = mido.open_output('CASIO USB-MIDI 1')

e2 = mido.Message('note_on', channel=0, note=40, velocity=64, time=0)
g2 = mido.Message('note_on', channel=0, note=43, velocity=64, time=0)
g_sharp2 = mido.Message('note_on', channel=0, note=44, velocity=64, time=0)
a3 = mido.Message('note_on', channel=0, note=45, velocity=64, time=0)
a_sharp3 = mido.Message('note_on', channel=0, note=46, velocity=64, time=0)
b3 = mido.Message('note_on', channel=0, note=47, velocity=64, time=0)
c3 = mido.Message('note_on', channel=0, note=48, velocity=64, time=0)
d3 = mido.Message('note_on', channel=0, note=50, velocity=64, time=0)
d_sharp3 = mido.Message('note_on', channel=0, note=51, velocity=64, time=0)
f3 = mido.Message('note_on', channel=0, note=53, velocity=64, time=0)
g3 = mido.Message('note_on', channel=0, note=55, velocity=64, time=0)
e3 = mido.Message('note_on', channel=0, note=52, velocity=64, time=0)

# chord_progression = [[a3], [c3, e3], [e2], [c3, a3]]

chord_progression = [[c3], [d_sharp3, g3], [a_sharp3], [d3, f3], [g_sharp2], [c3, d_sharp3], [g2], [b3, d3]]

interval_speed = 0.5

while True:
    for chord in chord_progression:
        for note in chord:
            outport.send(note)
        
        time.sleep(interval_speed)
        
        for note in chord:
            outport.send(mido.Message('note_off', note.note))

# def get_output_names():
#     print(mido.get_output_names())

# with mido.open_input() as port:
#     for message in  port:
#         print(message)

# print(mido.get_input_names())

#45 /// 48 52 /// 40 /// 48 52