import mido

# def get_note_ids(register=4):
#     note_ids = []
    
#     for i in range(1, 14):
#         note_ids.append((23 + i) + (register - 1) * 12)
        
#     return note_ids

def get_note_ids(mode=0, start=24, register=4):
    note_ids = []
    
    if mode == 0:
        steps = [0, 2, 2, 1, 2, 2, 2, 1]
    
    else:
        steps = [0, 2, 1, 2, 2, 1, 2, 2]
    
    current_id = start
    for i in steps:
        current_id += i
        note_ids.append((current_id) + (register - 1) * 12)
        
    return note_ids

def get_register(register=4):
    note_ids = get_note_ids(register)
        
    register = {
        "c"       : mido.Message('note_on', channel=0, note=note_ids[0], velocity=64, time=0),
        "c_sharp" : mido.Message('note_on', channel=0, note=note_ids[1], velocity=64, time=0),
        "d"       : mido.Message('note_on', channel=0, note=note_ids[2], velocity=64, time=0),
        "d_sharp" : mido.Message('note_on', channel=0, note=note_ids[3], velocity=64, time=0),
        "e"       : mido.Message('note_on', channel=0, note=note_ids[4], velocity=64, time=0),
        "f"       : mido.Message('note_on', channel=0, note=note_ids[5], velocity=64, time=0),
        "f_sharp" : mido.Message('note_on', channel=0, note=note_ids[6], velocity=64, time=0),
        "g"       : mido.Message('note_on', channel=0, note=note_ids[7], velocity=64, time=0),
        "g_sharp" : mido.Message('note_on', channel=0, note=note_ids[8], velocity=64, time=0),
        "a"       : mido.Message('note_on', channel=0, note=note_ids[9], velocity=64, time=0),
        "a_sharp" : mido.Message('note_on', channel=0, note=note_ids[10], velocity=64, time=0),
        "b"       : mido.Message('note_on', channel=0, note=note_ids[11], velocity=64, time=0),
    }
    
    return register

def generate_scale(key='c', mode='maj', register=4):
    
    return None

print(get_note_ids(1))
# print(get_register(4))