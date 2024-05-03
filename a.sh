#!/bin/bash

conda create --name tortoise python=3.9 numba inflect
conda activate tortoise
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install transformers=4.29.2

pip install tokenizers
pip install -r requirements.txt
python setup.py install

python main.py