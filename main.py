import soundcard as sc
import soundfile as sf
import pyperclip
import os
from pynput import keyboard

SAMPLE_RATE = 48000
OUTPUT_FILE_NAME = "out.wav"
is_recording = False

def on_press(key):
    global is_recording
    try:
        if key == keyboard.Key.f3:
            is_recording = not is_recording
            print("Starting..." if is_recording else "Stopping...")
    except AttributeError:
        pass

with keyboard.Listener(on_press = on_press) as listener:
    while True:
        with sc.get_microphone(id = str(sc.default_speaker().name),
                            include_loopback = True).recorder(samplerate = SAMPLE_RATE) as mic:

            data = []

            while is_recording:
                
                new_data = mic.record(numframes = int(SAMPLE_RATE * 0.1))
                data.extend(new_data[:, 0].tolist())

                if not is_recording:

                    sf.write(file = OUTPUT_FILE_NAME, data = data, samplerate = SAMPLE_RATE)

                    print("Copying to clipboard...")

                    file_path = os.path.abspath("out.wav")
                    normalized_path = os.path.normpath(file_path)
                    anki_path = f'file:///{normalized_path}'
                    pyperclip.copy(anki_path)

                    print("Copied.")
