from src.infrastructure.adapters.mido_adapter import MidoAdapter
from src.application.player_service import PlayerService
from src.domain.music_theory import get_scale_notes, get_playable_sequence, random_chord_sequence
from src.domain.bpm import get_interval_speed
from src.domain.progressions import c_major_7

midi_adapter = MidoAdapter(port_name="Midi Through:Midi Through Port-0 14:0")

player = PlayerService(port=midi_adapter)

bpm = 80
interval_speed = get_interval_speed(bpm=bpm, time_signature=1)

scale = get_scale_notes(mode=0, key=1, register=[3,4], include_octave=True)
#sequence = random_chord_sequence(scale=scale, chord_count=4, note_count=4)
#sequence = get_playable_sequence(scale)
sequence = c_major_7

print(f"A tocar sequencia {sequence}")
player.play_sequence(sequence=sequence, interval_speed=interval_speed, staccato=1)