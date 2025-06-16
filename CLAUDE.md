# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flask-based API server that provides OpenAI Whisper speech recognition capabilities through REST endpoints. The application is designed for cloud deployment with memory optimization considerations.

## Common Development Commands

### Running the Application Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask development server
python app.py

# Or use Gunicorn (production server)
gunicorn app:app
```

### Environment Variables
- `WHISPER_MODEL`: Model size (tiny, base, small, medium, large) - defaults to "tiny"
- `PORT`: Server port - defaults to 5000

### Testing the API
```bash
# Health check
curl http://localhost:5000/health

# Transcribe audio file
curl -X POST http://localhost:5000/transcribe \
  -F "audio=@sample/Audio 2_002_1S7X0H.L.wav" \
  -F "language=ja" \
  -F "task=transcribe"
```

## Architecture Overview

The application follows a simple single-file Flask architecture:

1. **Lazy Model Loading**: The Whisper model is loaded only when first needed to optimize memory usage during startup.

2. **Stateless API Design**: Each request is independent, with audio files processed in temporary storage and cleaned up after transcription.

3. **Deployment Flexibility**: Supports multiple deployment strategies:
   - Docker containers (Dockerfile)
   - Railway platform (railway.json, nixpacks.toml)
   - Render platform (start.sh)

4. **Memory Optimization**: Default configuration uses the "tiny" model to work within free-tier memory constraints (512MB on Render).

## Key Technical Decisions

- **Flask + Gunicorn**: Chosen for simplicity and production readiness
- **CORS enabled**: Allows cross-origin requests for web application integration
- **Temporary file handling**: Audio files are saved temporarily during processing to avoid memory issues with large files
- **Environment-based configuration**: Model size and port are configurable via environment variables for different deployment scenarios