import time
import threading

class PlayerService:
    def __init__(self, port):
        self.port = port
        self.playing = False
    
    def _play_sequence(self, sequence, interval_speed=0.5, staccato=0.5):
        note_duration = interval_speed * staccato
        silence_duration = interval_speed - note_duration
        
        for chord in sequence:
            for note_int in chord:
                self.port.send_note_on(note_int, 64)
            time.sleep(note_duration)
            
            for note_int in chord: 
                self.port.send_note_off(note_int)
            time.sleep(silence_duration)

    def _loop_sequence(self, sequence, interval_speed=0.5, staccato=0.5):
        note_duration = interval_speed * staccato
        silence_duration = interval_speed - note_duration
        
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

    def play_sequence(self, sequence, interval_speed=0.5, staccato=0.5):
        thread = threading.Thread(target=self._play_sequence, args=(sequence, interval_speed, staccato), daemon=True)
        thread.start()

    def loop_sequence(self, sequence, interval_speed=0.5, staccato=0.5):
        self.playing = False
        time.sleep(interval_speed)
        thread = threading.Thread(target=self._loop_sequence, args=(sequence, interval_speed, staccato), daemon=True)
        thread.start()
    
    def stop_loop(self):
        self.playing = False