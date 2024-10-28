import whisper

# Load the Whisper model
model = whisper.load_model("medium")  # Options: "tiny", "base", "small", "medium", "large"

# Path to your audio file in Portuguese
audio_file = "/home/joaopedromm/Desktop/hackaton/my_env/include/python3.12/audioEx.wav"  # Whisper supports multiple formats

# Transcribe the audio in Portuguese
transcription = model.transcribe(audio_file, language="pt")
transcription_text = transcription["text"]

# Save the transcription to a .txt file
with open("audioTranscrito.txt", "w", encoding="utf-8") as file:
    file.write("Transcription in Portuguese:\n")
    file.write(transcription_text)

print("Audio transcrito com sucesso!\n")