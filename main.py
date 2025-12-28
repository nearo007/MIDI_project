import mido
from scales import get_playable_scale
from ports import get_virtual_output_port, get_output_port, play_output
from utils import get_interval_speed

bpm = 120
interval_speed = get_interval_speed(bpm, 1)

output_port = mido.open_output(get_output_port())
output_port = mido.open_output(get_virtual_output_port())

scale = get_playable_scale(2, 1, 2) # mode (0=major, 1=minor), key 1-12 (C to B), register 1-7 (octaves)

play_output(output_port, scale, interval_speed, 0.5)