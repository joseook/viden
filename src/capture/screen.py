import mss
from PIL import Image

class ScreenCapture:
    def __init__(self):
        self.sct = mss.mss()

    def capture_full_screen(self):
        # Captura a tela inteira
        monitor = self.sct.monitors[1]
        screenshot = self.sct.grab(monitor)
        # Converte para objeto Image do Pillow
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        return img

    def capture_region(self, region):
        # region: (left, top, width, height)
        screenshot = self.sct.grab(region)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        return img

if __name__ == "__main__":
    cap = ScreenCapture()
    img = cap.capture_full_screen()
    img.save("test_capture.png")
    print("Captura de tela salva como test_capture.png")
