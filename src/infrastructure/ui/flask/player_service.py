from src.infrastructure.adapters.mido_adapter import MidoAdapter
from src.application.player_service import PlayerService

midi_adapter = MidoAdapter()
midi_adapter.pick_port()

player_service = PlayerService(port=midi_adapter)

if __name__ == '__main__':
    print("playing")
    player_service.play_sequence([[60]])