from abc import ABC, abstractmethod

class IMIDIPort(ABC):
    @abstractmethod
    def send_note_on(self, note: int, velocity: int):
        pass
    
    @abstractmethod
    def send_note_off(self, note: int):
        pass