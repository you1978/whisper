#!/bin/bash
# Install whisper and dependencies at runtime
pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
pip install --no-cache-dir git+https://github.com/openai/whisper.git

# Start the application
exec gunicorn app:app --bind 0.0.0.0:$PORT --timeout 300 --workers 1