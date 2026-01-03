#from src.infrastructure.adapters.mido_adapter import MidoAdapter
from ...adapters.mido_adapter import MidoAdapter

def user_choose(options):
    print()
    for o in range(len(options)):
        print(f"{o + 1}. {options[o]}")
    print()
    user_in = str(input(">> "))
    
    return user_in

def run():
    mido_adapter = MidoAdapter()
    
    while True: # app loop
        options = ["Choose output port.", "Generate chord progression.", "Loop scale."]
        
        user_in = user_choose(options)
        
        match user_in:
            case "1":
                ports = mido_adapter.available_outports()
                
                user_choose(ports)
            case "2":
                pass
            case "3":
                pass
            case _:
                pass
        
        if user_in == "quit":
            print("See ya, next time.")
            break;
        
run()