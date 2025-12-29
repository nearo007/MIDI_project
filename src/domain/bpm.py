def get_interval_speed(bpm, time_signature=1):
    bps = 60 / bpm
    return bps / time_signature