from src.infrastructure.adapters.mido_adapter import MidoAdapter
from src.application.player_service import PlayerService
from src.domain.music_theory import get_scale_notes, get_playable_scale
from src.domain.bpm import get_interval_speed

midi_adapter = MidoAdapter()

player = PlayerService(port=midi_adapter)

bpm = 120
interval_speed = get_interval_speed(bpm=bpm, time_signature=1)

scale = get_playable_scale(mode=1, key=1, register=2)

# scale = [[60, 64, 67], [57, 60, 64], [53, 57, 60], [55, 59, 62]] # testando acordes

print(f"A tocar escala {scale}")
player.play_sequence(scale, interval_speed)