#from src.infrastructure.adapters.mido_adapter import MidoAdapter
from ...adapters.mido_adapter import MidoAdapter
from ....domain.music_theory import get_scale_notes, get_playable_sequence, random_chord_sequence
from ....application.player_service import PlayerService
from ....domain.bpm import get_interval_speed

def str_to_int(user_in: str): #TODO cli_app out of scope
    try:
        user_in = int(user_in)
    
    except Exception as e:
        print("Invalid input.")
        
    return user_in

def display_options(options):
    print()
    for o in range(len(options)):
        print(f"{o + 1}. {options[o]}")
    print()
    
def user_choose(options):
    print()
    for o in range(len(options)):
        print(f"{o + 1}. {options[o]}")
    print()
    user_in = str(input(">> "))
    
    return user_in

def run():
    adapter = MidoAdapter()
    adapter.pick_port()
    
    while True: # app loop
        options = ["Choose output port.", "Generate chord progression.", "Loop scale."]
        
        display_options(options)
        print(f"Type \"quit\" to exit the CLI.")
        print()
        
        user_in = str(input(">> "))
        print()
        
        match user_in:
            case "1":
                ports = adapter.available_outports()
                
                user_in = user_choose(ports)
                port_id = str_to_int(user_in) - 1
                
                try:
                    adapter.set_outport(ports[port_id])
                    print()
                    print(f"Output port was successfully set to: {adapter.outport.name}")
                    
                except Exception as e:
                    print(e)
                
            case "2":
                print("\nEnter the following parameters:\n(Blank for default values)")
                
                print("\nEnter scale mode: ")
                options = ["Major", "Minor", "Minor Blues"]
                user_in = user_choose(options)
                mode = str_to_int(user_in)
                
                print("\nEnter scale key: ")
                options = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
                user_in = user_choose(options)
                key = str_to_int(user_in)
                
                print("\nEnter octave (1-7): ")
                user_in = str(input(">> "))
                octave = str_to_int(user_in)
                
                scale = get_scale_notes(mode=mode, key=key, octave=octave, include_octave=True) #TODO include octave hard coded
                
                sequence = random_chord_sequence(scale=scale, chord_count=4, note_count=3)
                player = PlayerService(adapter)
                
                bpm = 120 #TODO hard coded
                interval_speed = get_interval_speed(bpm)
                player.play_sequence(sequence=sequence, interval_speed=interval_speed, staccato=0.5) # staccato factor hard coded
                
            case "3":
                pass
            
            case "quit" | "Quit" | "QUIT":
                print("See you, next time.")
                break;
            
            case _:
                pass
        
run()