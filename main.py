import soundcard as sc
import soundfile as sf
import pyperclip
import keyboard
import os

output_file_name = "out.wav"
SAMPLE_RATE = 48000
SECONDS = 5
is_recording = False

# print("Starting recording...", end="")
# with sc.get_microphone(id = str(sc.default_speaker().name),
#                        include_loopback = True).recorder(samplerate = SAMPLE_RATE) as mic:
#     data = mic.record(numframes = SAMPLE_RATE * SECONDS)
#     print("Finished.")

#     sf.write(file = output_file_name, data = data[:, 0], samplerate = SAMPLE_RATE)

# file_path = os.path.abspath("out.wav")
# file_url = f'file://{file_path.replace(" ", "%20")}'

# # copy the file URL to the clipboard
# pyperclip.copy(file_url)
# print(f"File URL copied to clipboard: {file_url}")

while True:
    with sc.get_microphone(id = str(sc.default_speaker().name),
                        include_loopback = True).recorder(samplerate = SAMPLE_RATE) as mic:

        data = []

        if keyboard.is_pressed('f2'):
            is_recording = not is_recording
            print("Starting...")

        while is_recording:
            
            new_data = mic.record(numframes = int(SAMPLE_RATE * 0.1))
            data.extend(new_data[:, 0].tolist())
            #for i in data: big_data.append(i)

            if keyboard.is_pressed('f2'):
                is_recording = not is_recording
                sf.write(file = output_file_name, data = data, samplerate = SAMPLE_RATE)
                print("Stopped...")
                