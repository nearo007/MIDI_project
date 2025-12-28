import mido

def get_note_ids(mode, key, register):
    note_ids = []
    
    if mode == 0:
        steps = [0, 2, 2, 1, 2, 2, 2, 1]
    
    else:
        steps = [0, 2, 1, 2, 2, 1, 2, 2]
    
    current_id = key + 23
    for i in steps:
        current_id += i
        note_ids.append((current_id) + (register - 1) * 12)
        
    return note_ids

def get_scale(mode=0, key=1, register=3): # mode (0=major, 1=minor), key 1-12 (C to B), register 1-7 (octaves)
    note_ids = get_note_ids(mode, key, register)

    scale = [
        mido.Message('note_on', channel=0, note=note_ids[0], velocity=64, time=0),
        mido.Message('note_on', channel=0, note=note_ids[1], velocity=64, time=0),
        mido.Message('note_on', channel=0, note=note_ids[2], velocity=64, time=0),
        mido.Message('note_on', channel=0, note=note_ids[3], velocity=64, time=0),
        mido.Message('note_on', channel=0, note=note_ids[4], velocity=64, time=0),
        mido.Message('note_on', channel=0, note=note_ids[5], velocity=64, time=0),
        mido.Message('note_on', channel=0, note=note_ids[6], velocity=64, time=0),
        mido.Message('note_on', channel=0, note=note_ids[7], velocity=64, time=0)
    ]
    
    return scale

def get_playable_scale(mode=0, key=1, register=3):
    scale = get_scale(mode, key, register)
    
    playable_scale = []
    
    for i in scale:
        playable_scale.append([i])
    
    return playable_scale