import mido
from src.application.interfaces.midi_port import IMIDIPort

class MidoAdapter(IMIDIPort):
    def __init__(self, port_name=None):
        if port_name is None:
            ports = mido.get_output_names()
            print(ports)
            
            for o in ports:
                if o.find('MIDI') != -1:
                    port_name = o
                    break;
                
                if o.find('virtual') != -1:
                    port_name = o
            
            self.outport = mido.open_output(port_name)
        
    def send_note_on(self, note: int, velocity: int):
        msg = mido.Message('note_on', note=note, velocity=velocity)
        self.outport.send(msg)
    
    def send_note_off(self, note: int):
        msg = mido.Message('note_off', note=note, velocity=0)
        self.outport.send(msg)