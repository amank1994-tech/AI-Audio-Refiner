import gradio as gr
import whisper
from TTS.api import TTS
import tempfile

# Load models once
asr_model = whisper.load_model("small")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

def refine_audio(audio_path):
    # 1. Speech to text
    result = asr_model.transcribe(audio_path)
    raw_text = result["text"]

    # 2. Clean text (simple rule-based for demo)
    cleaned_text = raw_text.replace("um", "").replace("uh", "")

    # 3. Generate clean audio
    output_audio = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name
    tts.tts_to_file(
        text=cleaned_text,
        speaker_wav=audio_path,
        language="en",
        file_path=output_audio
    )

    return output_audio, cleaned_text

gr.Interface(
    fn=refine_audio,
    inputs=gr.Audio(type="filepath", label="Record your voice"),
    outputs=[
        gr.Audio(label="Refined Audio"),
        gr.Textbox(label="Cleaned Text")
    ],
    title="AI Audio Refiner",
    description="Record messy speech → get clear audio in your own voice"
).launch()
