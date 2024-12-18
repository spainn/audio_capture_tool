import soundcard as sc
import soundfile as sf
import pyperclip
import keyboard
import os
import urllib.parse

SAMPLE_RATE = 48000
OUTPUT_FILE_NAME = "out.wav"
is_recording = False

while True:
    with sc.get_microphone(id = str(sc.default_speaker().name),
                        include_loopback = True).recorder(samplerate = SAMPLE_RATE) as mic:

        data = []

        if keyboard.is_pressed('f3'):
            is_recording = not is_recording
            print("Starting...")

        while is_recording:
            
            new_data = mic.record(numframes = int(SAMPLE_RATE * 0.1))
            data.extend(new_data[:, 0].tolist())

            if keyboard.is_pressed('f3'):
                is_recording = not is_recording
                sf.write(file = OUTPUT_FILE_NAME, data = data, samplerate = SAMPLE_RATE)

                print("Stopped...")
                print("Copying to clipboard...")

                file_path = os.path.abspath("out.wav")
                normalized_path = os.path.normpath(file_path)
                anki_path = f'file:///{normalized_path}'
                pyperclip.copy(anki_path)

                print("Copied.")
