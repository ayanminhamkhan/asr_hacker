# from IPython import display as disp
import torch
import torchaudio
import numpy as np
from denoiser import pretrained
from denoiser.dsp import convert_audio
import os
from scipy.io import wavfile

# file u want named voice.mp3 in this folder
# 
name = input("audio file name: ")
model = pretrained.dns64().cuda()
wav, sr = torchaudio.load(f'{name}.mp3')
wav = convert_audio(wav.cuda(), sr, model.sample_rate, model.chin)
with torch.no_grad():
    denoised = model(wav[None])[0]
denoised_audio = denoised.data.cpu().numpy()

print(denoised_audio)
# print(denoised_audio.type())


# #splitting
# duration = len(denoised_audio) // 3
# parts = []
# for i in range(3):
#     part = denoised_audio[i * duration : (i + 1) * duration]
#     parts.append(part)

# #saving
# sample_rate = 44100
# for i, part in enumerate(parts):
#     # part.export(os.path.join(output_dir, f"part_{i+1}.wav"), format="wav")
#     # scaled = np.int16(part / np.max(np.abs(part)) * 32767)
#     # wavfile.write(output_dir + f'part_{i+1}.wav', sample_rate, part)
#     torchaudio.save(output_dir + f'/part_{i+1}.wav', part.cpu(), model.sample_rate)


output_dir = f"tortoise/voices/{name}"
os.makedirs(output_dir, exist_ok=True)
num_segments = 3
segment_length = denoised.size(1) // num_segments

# Store each segment to a separate file
for i in range(num_segments):
    segment = denoised[:, i * segment_length: (i + 1) * segment_length]
    torchaudio.save(output_dir + f'/denoised_segment_{i+1}.wav', segment.cpu(), model.sample_rate)

text = input("Enter text to be spoken: ")
os.system(f"python tortoise/do_tts.py --text \"{text}\" --voice {name} --preset fast")

