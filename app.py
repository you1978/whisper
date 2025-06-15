import os
import tempfile
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Lazy load Whisper model
MODEL_NAME = os.environ.get('WHISPER_MODEL', 'tiny')
model = None

def get_model():
    global model
    if model is None:
        import whisper
        model = whisper.load_model(MODEL_NAME)
    return model

ALLOWED_EXTENSIONS = {'mp3', 'mp4', 'mpeg', 'mpga', 'm4a', 'wav', 'webm'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "model": MODEL_NAME}), 200

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    file = request.files['audio']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if not allowed_file(file.filename):
        return jsonify({"error": "Invalid file format. Supported formats: " + ", ".join(ALLOWED_EXTENSIONS)}), 400
    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp_file:
            file.save(tmp_file.name)
            
            # Get optional parameters
            language = request.form.get('language', None)
            task = request.form.get('task', 'transcribe')  # 'transcribe' or 'translate'
            
            # Transcribe audio
            result = get_model().transcribe(
                tmp_file.name,
                language=language,
                task=task
            )
            
            # Clean up temp file
            os.unlink(tmp_file.name)
            
            return jsonify({
                "text": result["text"],
                "language": result.get("language"),
                "segments": result.get("segments", [])
            }), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "service": "Whisper API Server",
        "version": "1.0.0",
        "endpoints": {
            "/health": "GET - Health check",
            "/transcribe": "POST - Transcribe audio file"
        },
        "supported_formats": list(ALLOWED_EXTENSIONS),
        "model": MODEL_NAME
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)