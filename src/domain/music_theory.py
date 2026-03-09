from src.domain.notes import b0, scale_shapes
import random

def get_scale_notes(mode=0, key=1, octave=4, register=None, include_octave=False): # mode (0=major, 1=minor, 2=minor blues, 3=chromatic), key 1-12 (C to B), octave 1-7 (octaves)
    scale = []
    
    steps = scale_shapes[mode]
    
    if not include_octave:
        steps = steps[:-1]
        
    current_id = b0 + key
    
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

def get_chord(scale=get_scale_notes(mode=3), tonality=0, seventh=0): #tonality 0=maj 1=min, seventh 0=off 1=maj 2=min
    steps = []
    
    if tonality == 0:
        steps.extend([0, 4, 7])

    elif tonality == 1:
        steps.extend([0, 3, 7])
    
    if seventh == 1:
        steps.append(11)
    
    elif seventh == 2:
        steps.append(10)
    
    sequence = []
    
    for step in steps:
        sequence.append(scale[step])
        
    return sequence # [[0, 4, 7], [65, 75, 93, 120], [0, 4, 7], [69, 75, 97, 135]]