from src.infrastructure.adapters.mido_adapter import MidoAdapter
from src.application.player_service import PlayerService
from src.domain.music_theory import get_scale_notes, get_playable_sequence, random_chord_sequence
from src.domain.bpm import get_interval_speed

midi_adapter = MidoAdapter()

player = PlayerService(port=midi_adapter)

bpm = 120
interval_speed = get_interval_speed(bpm=bpm, time_signature=1)

sequence = get_playable_sequence(get_scale_notes(mode=2, key=1, register=[3, 5], include_octave=True))
# sequence = get_playable_sequence(get_scale_notes(mode=0, key=1, octave=4, include_octave=True))

print(f"A tocar sequencia {sequence}")
player.play_sequence(sequence=sequence, interval_speed=interval_speed, staccato=1)