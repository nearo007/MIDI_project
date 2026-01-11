import mido
from ...application.interfaces.midi_port import IMIDIPort

class MidoAdapter(IMIDIPort):
    def __init__(self, port_name=None):
        self._port_name = port_name
        self.outport = None
    
    def pick_port(self): # pick default with keywords "midi" and "virtual" taking priority
        if self._port_name is None:            
            ports = self.available_outports()
            
            if not ports:
                raise RuntimeError("No available port.")
            
            self._port_name = ports[0]
            
            for o in ports:
                name = o.lower()
                if 'midi' in name:
                    self._port_name = o
                    break;
                
                if 'virtual' in name:
                    self._port_name = o
            
            if self._port_name is None:
                raise RuntimeError("No available port.")
            
        self.set_outport(self._port_name)
    
    def available_outports(self) -> list[str]:
        return mido.get_output_names()
    
    def close_current_outport(self):
        if self.outport is not None:
            self.outport.close()
            
    def set_outport(self, output_port_name):
        self.close_current_outport()

        try:
            self.outport = mido.open_output(output_port_name)
        
        except IOError as e:
            raise RuntimeError(f"Failed to open output port in {output_port_name}") from e
        
    def send_note_on(self, note: int, velocity: int):
        if not self.outport:
            raise RuntimeError("No available port.")
        
        msg = mido.Message('note_on', note=note, velocity=velocity)
        self.outport.send(msg)
    
    def send_note_off(self, note: int):
        if not self.outport:
            raise RuntimeError("No available port.")
        msg = mido.Message('note_off', note=note, velocity=0)
        self.outport.send(msg)
    
    def get_current_port(self):
        return self._port_name
    
    def __del__(self):
        try:
            self.close_current_outport()
        
        except:
            pass