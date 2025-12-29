from src.domain.notes import b0

def get_scale_notes(mode, key, register): # mode (0=major, 1=minor), key 1-12 (C to B), register 1-7 (octaves)
    scale = []
    
    if mode == 0:
        steps = [0, 2, 2, 1, 2, 2, 2, 1] # major
    
    elif mode == 1:
        steps = [0, 2, 1, 2, 2, 1, 2, 2] # minor
    
    elif mode == 2:
        steps = [0, 3, 2, 1, 1, 3, 2] # minor blues
        
    current_id = b0 + key
    
    for i in steps:
        current_id += i
        scale.append((current_id) + (register - 1) * 12)
        
    return scale

def get_playable_scale(mode=0, key=1, register=3):
    scale = get_scale_notes(mode, key, register)
    
    playable_scale = []
    
    for i in scale:
        playable_scale.append([i])
    
    return playable_scale