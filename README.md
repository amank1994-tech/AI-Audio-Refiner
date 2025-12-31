# AI Audio Refiner 🎙️

An end-to-end AI application that converts raw, unstructured speech into clear and refined audio while preserving the original speaker’s voice.

## 🔍 What This Project Does
- Transcribes speech to text using automatic speech recognition (ASR)
- Cleans and refines the transcribed text
- Generates improved audio using voice cloning
- Provides a simple web interface for recording and playback

## 🛠️ Tech Stack
- Whisper (Speech-to-Text)
- Coqui XTTS v2 (Voice Cloning / TTS)
- Python
- Gradio (Web UI)

## 🚧 Challenges Faced
- Separating frontend UI from backend AI logic
- Connecting multiple AI components into a single pipeline
- Managing audio formats and file handling
- Debugging end-to-end integration issues

## ▶️ How to Run Locally
```bash
pip install -r requirements.txt
python app.py


