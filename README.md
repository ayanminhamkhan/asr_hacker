# Vocal-Vartalap_Tortoise_TTS
We use [Tortoise-TTS](https://github.com/neonbjb/tortoise-tts.git) and [denoiser](https://github.com/facebookresearch/denoiser) for  TTS model trained on our voice for hacker assignment


## Steps to run the project

To run code do follows
``` sh
conda create --name tortoise python=3.9 numba inflect
conda activate tortoise
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install transformers=4.29.2


pip install tokenizers
pip install -r requirements.txt
python setup.py install
```
Then to record voice samples run

```sh
python record.py
```

in the window formed in browser save the audio path as "./name.mp3" 
run 
```sh
python main.py
```
when asked for audio voice give the same name used above
and give the string you want to convert into audio

If you want to use an audio sample without recording put the file_name.mp3 in the folder with main.py and run
```sh
python main.py
```

The results will be stored in results/name (whichever audio file name you chose) folder

To compare audio before and after denoiser compare the audio file given/made (using record.py) with audio samples in tortoise/voices/audio_name folder



