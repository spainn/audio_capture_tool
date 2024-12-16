import soundcard as sc
import soundfile as sf
import pyperclip
import os

output_file_name = "out.wav"
SAMPLE_RATE = 48000
SECONDS = 5

print("Starting recording...", end="")
with sc.get_microphone(id = str(sc.default_speaker().name),
                       include_loopback = True).recorder(samplerate = SAMPLE_RATE) as mic:
    data = mic.record(numframes = SAMPLE_RATE * SECONDS)
    print("Finished.")

    sf.write(file = output_file_name, data = data[:, 0], samplerate = SAMPLE_RATE)

file_path = os.path.abspath("out.wav")
file_url = f'file://{file_path.replace(" ", "%20")}'

# copy the file URL to the clipboard
pyperclip.copy(file_url)
print(f"File URL copied to clipboard: {file_url}")