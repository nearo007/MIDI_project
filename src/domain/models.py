from dataclasses import dataclass

@dataclass
class NoteEvent:
    pitch: int
    velocity: 64
    duration: 0.5