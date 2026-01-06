from .notes import b0
import random

def get_scale_notes(mode=0, key=1, octave=4, register=None, include_octave=False): # mode (0=major, 1=minor), key 1-12 (C to B), octave 1-7 (octaves)
    scale = []
    
    if mode == 0:
        steps = [0, 2, 2, 1, 2, 2, 2, 1] # major
    
    elif mode == 1:
        steps = [0, 2, 1, 2, 2, 1, 2, 2] # minor
    
    elif mode == 2:
        steps = [0, 3, 2, 1, 1, 3, 2] # minor blues
    
    current_id = b0 + key
    if not include_octave:
        steps = steps[:-1]
    
    if register is not None:
        octave = register[0]
        
        while octave <= register[-1]:
            current_id = b0 + key
            for i in steps:
                current_id += i
                scale.append((current_id) + (octave - 1) * 12)
                
            octave += 1
    
    else:
        for i in steps:
            current_id += i
            scale.append((current_id) + (octave - 1) * 12)
    
    if include_octave and register is not None:
        scale = list(set(scale))
        
    return scale # [60, 64, 67]

def to_playable_sequence(sequence: list):    
    playable_scale = []
    
    for i in sequence:
        playable_scale.append([i])
    
    return playable_scale # [[60, 64, 67], [57, 60, 64], [53, 57, 60], [55, 59, 62]]

def random_chord_sequence(scale=None, chord_count=4, note_count=3):
    if not scale:
        scale = get_scale_notes()
        
    sequence = []
    
    for _ in range(chord_count):
        available_notes = scale.copy()
        chord = random.sample(available_notes, note_count)
    
        sequence.append(chord)
    
    return sequence # [[60, 64, 67], [57, 60, 64], [53, 57, 60], [55, 59, 62]]