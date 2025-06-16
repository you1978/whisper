#!/usr/bin/env python3
"""Create a simple test audio file"""

import numpy as np
import wave

# Create a 1 second silent WAV file
sample_rate = 16000
duration = 1  # seconds
samples = np.zeros(int(sample_rate * duration), dtype=np.int16)

# Save as WAV file
with wave.open('test_audio.wav', 'w') as wav_file:
    wav_file.setnchannels(1)  # mono
    wav_file.setsampwidth(2)  # 16-bit
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(samples.tobytes())

print("Created test_audio.wav (1 second silent audio)")