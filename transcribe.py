import whisper

# Load Whisper model once at startup
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """Transcribe audio file into text using Whisper"""
    result = model.transcribe(audio_path)
    return result["text"]
