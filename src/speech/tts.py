from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class TextToSpeech:
    def __init__(self, api_key=None):
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)

    def speak(self, text, output_file="response.mp3"):
        if not text:
            return None
            
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        response.stream_to_file(output_file)
        return output_file

    def play_audio(self, file_path):
        # Utiliza o player padrão do sistema ou biblioteca específica
        if os.name == 'nt':
            os.system(f"start {file_path}")
        else:
            os.system(f"afplay {file_path}")

if __name__ == "__main__":
    tts = TextToSpeech()
    # file = tts.speak("Olá, eu sou o Viden. Como posso ajudar?")
    # tts.play_audio(file)
