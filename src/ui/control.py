import keyboard
import time

class VidenControl:
    def __init__(self):
        self.active = False
        # Atalho para alternar entre ativo e mudo
        keyboard.add_hotkey('ctrl+shift+v', self.toggle_active)

    def toggle_active(self):
        self.active = not self.active
        status = "ATIVO" if self.active else "MUDO"
        print(f"\n[Viden] Status: {status}")

    def is_active(self):
        return self.active

if __name__ == "__main__":
    ctrl = VidenControl()
    print("Viden Control iniciado. Pressione Ctrl+Shift+V para alternar.")
    while True:
        time.sleep(1)
