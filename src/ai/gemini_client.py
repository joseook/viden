import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

class GeminiMultimodal:
    def __init__(self, api_key=None):
        api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Google API Key não encontrada.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash-exp') # Ou outra versão estável

    def process_query(self, prompt, image, audio_data=None):
        # image deve ser um objeto PIL.Image
        # audio_data (bytes) ainda não é suportado diretamente via bytes no SDK simples para Gemini 
        # (geralmente precisa de upload para File API), mas frames de vídeo/imagem funcionam bem.
        # Para v1.0, focaremos em Imagem + Texto. Áudio será transcrito ou enviado via File API se necessário.
        
        contents = [prompt, image]
        
        response = self.model.generate_content(contents)
        return response.text

if __name__ == "__main__":
    # Teste rápido (precisa de API_KEY)
    try:
        ai = GeminiMultimodal()
        print("Model inicializado.")
    except Exception as e:
        print(f"Erro ao inicializar IA: {e}")
