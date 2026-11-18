import sounddevice as sd
import numpy as np

print(sd.query_devices())
print("Default input:", sd.default.device[0])

audio = sd.rec(5 * 16000, samplerate=16000, channels=1, dtype="float32")
sd.wait()

print("Peak level:", np.max(np.abs(audio)))
sd.play(audio, 16000)
sd.wait()
