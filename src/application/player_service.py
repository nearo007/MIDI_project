import time

class PlayerService:
    def __init__(self, port):
        self.port = port
    
    def play_sequence(self, sequence, interval_speed=0.5, staccato=0.5):
        note_duration = interval_speed * staccato
        silence_duration = interval_speed - note_duration
        
        for chord in sequence:
            for note_int in chord:
                self.port.send_note_on(note_int, 64)
            time.sleep(note_duration)
            
            for note_int in chord: 
                self.port.send_note_off(note_int)
            time.sleep(silence_duration)