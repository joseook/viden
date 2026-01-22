import pyaudio
import wave
import threading
import queue

class AudioCapture:
    def __init__(self, rate=16000, chunk=1024):
        self.rate = rate
        self.chunk = chunk
        self.format = pyaudio.paInt16
        self.channels = 1
        self.p = pyaudio.PyAudio()
        self.frames = []
        self.is_recording = False
        self.stream = None

    def start_recording(self):
        self.is_recording = True
        self.frames = []
        self.stream = self.p.open(format=self.format,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk,
                                  stream_callback=self._callback)
        self.stream.start_stream()

    def _callback(self, in_data, frame_count, time_info, status):
        if self.is_recording:
            self.frames.append(in_data)
        return (in_data, pyaudio.paContinue)

    def stop_recording(self):
        self.is_recording = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        return self.get_audio_data()

    def get_audio_data(self):
        return b''.join(self.frames)

    def save_wav(self, filename, data):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(data)
        wf.close()

if __name__ == "__main__":
    import time
    audio = AudioCapture()
    print("Gravando 3 segundos...")
    audio.start_recording()
    time.sleep(3)
    data = audio.stop_recording()
    audio.save_wav("test_audio.wav", data)
    print("Áudio salvo como test_audio.wav")
