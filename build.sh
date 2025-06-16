#!/bin/bash
set -e

# Install CPU-only PyTorch
pip install torch==2.1.2+cpu torchaudio==2.1.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Install other requirements
pip install -r requirements-base.txt