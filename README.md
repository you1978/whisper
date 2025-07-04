# Whisper API Server

OpenAI Whisperを使用した音声認識APIサーバー

## Renderへのデプロイ

1. このリポジトリをGitHubにプッシュ
2. [Render](https://render.com)でNew Web Serviceを作成
3. GitHubリポジトリを接続
4. 設定:
   - Build Command: デフォルト（`pip install -r requirements.txt`）
   - Start Command: `./start.sh`
5. 環境変数を設定:
   - `WHISPER_MODEL`: tiny（メモリ制限のため）
   - `PYTHON_VERSION`: 3.11.10
6. 無料プランの場合は512MBメモリ制限があるため、tinyモデルのみ使用可能

## Railwayへのデプロイ

1. このリポジトリをGitHubにプッシュ
2. [Railway](https://railway.app)でNew Projectを作成
3. "Deploy from GitHub repo"を選択
4. 環境変数を設定（任意）:
   - `WHISPER_MODEL`: 使用するモデル (tiny, base, small, medium, large) デフォルト: base
   - `PORT`: Railwayが自動設定

## API使用方法

### ヘルスチェック
```bash
curl https://whisper-jbtf.onrender.com/health
```

### 音声ファイルの文字起こし
```bash
curl -X POST https://whisper-jbtf.onrender.com/transcribe \
  -F "audio=@your-audio-file.mp3" \
  -F "language=ja" \
  -F "task=transcribe"
```

パラメータ:
- `audio`: 音声ファイル (必須)
- `language`: 言語コード (任意, 例: ja, en)
- `task`: transcribe または translate (任意, デフォルト: transcribe)

対応フォーマット: mp3, mp4, mpeg, mpga, m4a, wav, webm