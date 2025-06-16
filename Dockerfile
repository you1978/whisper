FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first for better caching
COPY requirements.txt .

# Install Python dependencies (without PyTorch)
RUN pip install --no-cache-dir -r requirements.txt

# Install CPU-only PyTorch to reduce image size
RUN pip install --no-cache-dir \
    torch==2.1.2+cpu \
    torchaudio==2.1.2+cpu \
    -f https://download.pytorch.org/whl/torch_stable.html

# Copy application code
COPY app.py .

# Create a non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 5000

# Run the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--timeout", "300", "--workers", "1"]