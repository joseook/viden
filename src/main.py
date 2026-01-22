import time
import threading
from src.capture.screen import ScreenCapture
from src.capture.audio import AudioCapture
from src.ai.gemini_client import GeminiMultimodal
from src.speech.tts import TextToSpeech
from src.ui.control import VidenControl

class VidenApp:
    def __init__(self):
        self.screen = ScreenCapture()
        self.audio = AudioCapture()
        self.ai = GeminiMultimodal()
        self.tts = TextToSpeech()
        self.control = VidenControl()
        self.is_running = True

    def run(self):
        print("Viden v1.0 iniciado.")
        print("Atalho: Ctrl+Shift+V para Ativar/Desativar.")
        
        try:
            while self.is_running:
                if self.control.is_active():
                    self.process_cycle()
                else:
                    time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nEncerrando Viden...")
            self.is_running = False

    def process_cycle(self):
        print("[Viden] Capturando contexto...")
        # 1. Capturar Tela
        frame = self.screen.capture_full_screen()
        
        # 2. Capturar Áudio (simulado ou por gatilho de voz no futuro)
        # Para v1.0 simplificada, enviaremos apenas a tela com um prompt fixo 
        # se o áudio não estiver sendo processado em tempo real por streaming
        
        prompt = "Analise minha tela. Identifique a linguagem de programação, o código atual e se há algum erro visível no console. Seja conciso na resposta."
        
        print("[Viden] Consultando IA...")
        try:
            response_text = self.ai.process_query(prompt, frame)
            print(f"[Viden] IA: {response_text}")
            
            # 3. Responder via Voz
            print("[Viden] Gerando voz...")
            audio_file = self.tts.speak(response_text)
            if audio_file:
                self.tts.play_audio(audio_file)
        except Exception as e:
            print(f"[Erro] Falha no processamento: {e}")
        
        # Espera um pouco antes do próximo ciclo para evitar consumo excessivo
        # No futuro, isso será gatilhado por voz
        time.sleep(5) 

if __name__ == "__main__":
    app = VidenApp()
    app.run()
