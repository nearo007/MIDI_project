import time
import threading
from src.domain.bpm import get_interval_speed

class PlayerService:
    def __init__(self, port):
        self.port = port
        self.playing = False
        self.interval_speed = 0.5
        self.staccato_value = 0.5
    
    def set_bpm(self, bpm=100, time_signature=1):
        interval_speed = get_interval_speed(bpm=bpm, time_signature=time_signature)
        self.interval_speed = interval_speed
    
    def set_staccato(self, staccato_value):
        self.staccato_value = staccato_value
    
    def _play_sequence(self, sequence):
        note_duration = self.interval_speed * self.staccato_value
        silence_duration = self.interval_speed - note_duration
        
        for chord in sequence:
            for note_int in chord:
                self.port.send_note_on(note_int, 64)
            time.sleep(note_duration)
            
            for note_int in chord: 
                self.port.send_note_off(note_int)
            time.sleep(silence_duration)

    def _loop_sequence(self, sequence):
        note_duration = self.interval_speed * self.staccato_value
        silence_duration = self.interval_speed - note_duration
        
        self.playing = True
        
        while (self.playing == True):
            for chord in sequence:
                if not self.playing:
                    return
                
                for note_int in chord:
                    self.port.send_note_on(note_int, 64)
                time.sleep(note_duration)
                
                for note_int in chord: 
                    self.port.send_note_off(note_int)
                time.sleep(silence_duration)

    def play_sequence(self, sequence):
        thread = threading.Thread(target=self._play_sequence, args=([sequence]), daemon=True)
        thread.start()

    def loop_sequence(self, sequence):
        self.playing = False
        time.sleep(self.interval_speed)
        thread = threading.Thread(target=self._loop_sequence, args=([sequence]), daemon=True)
        thread.start()
    
    def stop_loop(self):
        self.playing = False