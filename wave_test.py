from pydub import AudioSegment
from gtts import gTTS
import os

# Function to generate audio files
def generate_audio(text, output_dir, file_format='wav'):
    tts = gTTS(text)
    temp_file = os.path.join(output_dir, 'temp.mp3')
    tts.save(temp_file)

    audio = AudioSegment.from_mp3(temp_file)
    output_file = os.path.join(output_dir, f"{text}.{file_format}")

    if file_format == 'wav':
        audio.export(output_file, format='wav')
    else:
        audio.export(output_file, format='mp3')

    os.remove(temp_file)

# Example usage
output_directory = 'audio'
os.makedirs(output_directory, exist_ok=True)
generate_audio('hello', output_directory, file_format='wav')