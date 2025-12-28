import mido

def get_note_ids(mode, key, register):
    note_ids = []
    
    if mode == 0:
        steps = [0, 2, 2, 1, 2, 2, 2, 1] # major
    
    elif mode == 1:
        steps = [0, 2, 1, 2, 2, 1, 2, 2] # minor
    
    elif mode == 2:
        steps = [0, 3, 2, 1, 1, 3, 2] # minor blues
    B0_MIDI = 23
    current_id = B0_MIDI + key
    for i in steps:
        current_id += i
        note_ids.append((current_id) + (register - 1) * 12)
        
    return note_ids

def get_scale(mode=0, key=1, register=3): # mode (0=major, 1=minor), key 1-12 (C to B), register 1-7 (octaves)
    note_ids = get_note_ids(mode, key, register)

    scale = []
    for i in note_ids:
        scale.append(mido.Message('note_on', channel=0, note=i, velocity=64, time=0))
    
    return scale

def get_playable_scale(mode=0, key=1, register=3):
    scale = get_scale(mode, key, register)
    
    playable_scale = []
    
    for i in scale:
        playable_scale.append([i])
    
    return playable_scale