#!/usr/bin/env bash
# Install system dependencies
apt-get update && apt-get install -y ffmpeg git

# Upgrade pip
python -m pip install --upgrade pip

# Install CPU-only torch first
pip install torch==2.0.1+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

# Install other dependencies
pip install flask==3.0.0 flask-cors==4.0.0 gunicorn==21.2.0 ffmpeg-python==0.2.0

# Install whisper last
pip install openai-whisper==20230314