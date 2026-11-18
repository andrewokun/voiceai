# Voice AI

A 100% local voice assistant that uses your voice to prompt your llm.

## Requirements

- Python 3.10+
- A working microphone
- [Ollama](https://ollama.com/)
- Enough system memory and processing power to run the selected models

## Setup

### 1. Install system audio dependencies

```bash
sudo apt update
sudo apt install libportaudio2 portaudio19-dev python3-venv
```

### 2. Clone the github repository
```bash
git clone https://github.com/andrewokun/voiceai
```

### 3. create a virtual environment and install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. make sure that your microphone is enabled
go to settings and make sure microphone input is enabled

### 5. run the script
```bash
python3 src/main.py
```
