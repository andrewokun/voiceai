# Voice AI

A 100% local voice assistant that uses your voice to prompt your llm.

## Requirements

- Python 3.10+
- A working microphone
- [Ollama](https://ollama.com/)
- Enough system memory and processing power to run a llm

## Setup

### 1. Install system audio dependencies

```bash
sudo apt update
sudo apt install libportaudio2 portaudio19-dev python3-venv
```
### 2. Install Ollama

go to [Ollama.com](https://ollama.com/) and install ollama for your os


### 3. Clone the github repository
```bash
git clone https://github.com/andrewokun/voiceai
```

### 4. create a virtual environment and install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. edit the config.py file in the src folder to your needs

```bash
# config.py

model_name = "gemma3:270m" # change this to be the model that you want to use
listening_time = float(5) # increase this number for the whisper model to listen to you for longer

```

### 6. make sure that your microphone is enabled
go to your device settings and make sure microphone input is enabled

### 7. run the script
```bash
python3 src/main.py
```
