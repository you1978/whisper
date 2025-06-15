#!/usr/bin/env bash
# Install system dependencies
apt-get update && apt-get install -y ffmpeg

# Upgrade pip and setuptools
pip install --upgrade pip setuptools wheel

# Install Python dependencies
pip install -r requirements.txt