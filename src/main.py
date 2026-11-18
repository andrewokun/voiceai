import sounddevice as sd
from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu", compute_type="int8")

def listen(seconds=10):
    print("Listening...")
    audio = sd.rec(int(seconds * 16000), samplerate=16000, channels=1)
    sd.wait()
    segments, _ = model.transcribe(audio.flatten())
    return " ".join(s.text.strip() for s in segments)

text = listen()
print("You said:", text)
