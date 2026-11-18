import sounddevice as sd
from faster_whisper import WhisperModel
import ai_handler as ai
import time
from config import *

SAMPLE_RATE = 16000
model = WhisperModel("base", device="cpu", compute_type="int8")

def listen(seconds=listening_time):
    print("Listening...")
    audio = sd.rec(
        int(seconds * 16000),
        samplerate=16000,
        channels=1,
        dtype="float32",
    )
    sd.wait()

    segments, info = model.transcribe(
        audio.flatten(),
        language="en",
        vad_filter=True,
    )
    segments = list(segments)  # Run transcription before inspecting results.

    #print("Detected language:", info.language)
    #print("Raw segments:", [s.text for s in segments])
    return " ".join(s.text.strip() for s in segments)

#start_listen = time.time()

text = listen()
print("You said:", text)

#end_listen = time.time()

#listen_time = end_listen - start_listen

final_prompt = f"{text} \nOutput the result in less than 2 sentences to keep it simple"


#start_ai = time.time()
response = ai.send_prompt(final_prompt, model_name)
print(response)
#end_ai = time.time()

#ai_time = end_ai - start_ai

#print(f"Listen Time: {listen_time} Seconds")
#print(f"AI Time: {ai_time} Seconds")
