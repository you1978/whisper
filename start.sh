#!/bin/bash
set -e

# Install dependencies if not already installed
if ! python -c "import torch" 2>/dev/null; then
    echo "Installing PyTorch CPU version..."
    pip install torch==2.1.2+cpu torchaudio==2.1.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
fi

if ! python -c "import flask" 2>/dev/null; then
    echo "Installing other dependencies..."
    pip install -r requirements-base.txt
fi

# Start the application
exec gunicorn app:app --bind 0.0.0.0:$PORT --timeout 300 --workers 1