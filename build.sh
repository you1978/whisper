#!/usr/bin/env bash
# Install system dependencies
apt-get update && apt-get install -y ffmpeg git

# Upgrade pip
python -m pip install --upgrade pip

# Install dependencies one by one
pip install flask==3.0.0
pip install flask-cors==4.0.0
pip install gunicorn==21.2.0
pip install ffmpeg-python==0.2.0

# Install PyTorch CPU version
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install whisper from GitHub
pip install git+https://github.com/openai/whisper.git