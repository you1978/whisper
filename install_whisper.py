#!/usr/bin/env python3
"""Install Whisper with CPU-only PyTorch at runtime"""

import subprocess
import sys

def install_packages():
    """Install PyTorch CPU and Whisper"""
    print("Installing CPU-only PyTorch...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--no-cache-dir",
        "torch==2.1.2+cpu", "torchaudio==2.1.2+cpu",
        "-f", "https://download.pytorch.org/whl/torch_stable.html"
    ])
    
    print("Installing OpenAI Whisper...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "--no-cache-dir",
        "openai-whisper==20231117"
    ])
    
    print("Installation complete!")

if __name__ == "__main__":
    install_packages()