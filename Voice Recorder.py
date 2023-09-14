# before running the program install the library pyaudio using pip install pyaudio

import pyaudio
import wave

def record_audio(filename, duration=10):
    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 2
    fs = 44100

    audio = pyaudio.PyAudio()

    stream = audio.open(format=sample_format,
                        channels=channels,
                        rate=fs,
                        frames_per_buffer=chunk,
                        input=True)

    print("Recording...")

    frames = []

    for _ in range(0, int(fs / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(sample_format))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    filename = "recorded_audio.wav"
    duration = int(input("Enter recording duration (in seconds): "))
    record_audio(filename, duration)
    print(f"Audio saved as {filename}")
