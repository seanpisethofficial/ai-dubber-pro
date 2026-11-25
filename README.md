# AI DUBBER PRO v2.1.0

## SUPREME ULTRAMAX INFINITY — MICROSOFT KHMER VOICE EDITION

**Intelligent Voice. Perfect Synchronization.**

Enterprise-grade AI Video Dubbing Platform with Microsoft Azure Khmer Neural TTS.

---

## Features

- **Automatic Speech Recognition** — Transcribe dialogue from video using AI
- **Speaker Diarization** — Identify and track distinct speakers
- **Khmer Translation** — Natural, cinematic, formal, and casual Khmer translation modes
- **Microsoft Azure Neural TTS** — Professional Khmer voices (Sreymom Neural & Piseth Neural)
- **Auto-Fit Speed Engine** — Intelligent dialogue duration optimization
- **Audio Engineering** — Mixing, normalization, synchronization
- **Subtitle Studio** — SRT/VTT import, export, and editing
- **Professional Timeline** — Multitrack editing workspace
- **Export Center** — MP4/WebM/WAV/MP3 with preset export profiles
- **One-Click Auto Dubbing** — 16-phase automated pipeline

## Architecture

| Component | Technology |
|-----------|------------|
| Frontend | Next.js 14, React, TypeScript, Tailwind CSS |
| Backend | Python 3.12, FastAPI, SQLAlchemy |
| Database | SQLite (async via aiosqlite) |
| Media | FFmpeg 9.x, FFprobe |
| TTS | Microsoft Azure AI Speech SDK |
| ASR | Google Gemini API |
| Translation | Google Gemini API |

## Quick Start

### Prerequisites

- Node.js 20+ (LTS)
- Python 3.12+
- FFmpeg 6+

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/macOS

pip install -r requirements.txt

# Configure environment
copy .env.example .env
# Edit .env with your API keys

# Start backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Access the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

## API Keys Required

### Microsoft Azure Speech (TTS — Required for voice generation)
1. Create an Azure account at https://azure.microsoft.com
2. Create a Speech resource in Azure Portal
3. Copy the Key and Region
4. Set `AZURE_SPEECH_KEY` and `AZURE_SPEECH_REGION` in `.env`

### Google Gemini (ASR & Translation — Required for transcription and translation)
1. Get an API key from https://aistudio.google.com/apikey
2. Set `GEMINI_API_KEY` in `.env`

## Khmer Neural Voices

| Voice | ID | Gender | Locale |
|-------|-----|--------|--------|
| Microsoft Sreymom | `km-KH-SreymomNeural` | Female | km-KH |
| Microsoft Piseth | `km-KH-PisethNeural` | Male | km-KH |

## Project Structure

```
AI DUBBER PRO/
├── backend/
│   ├── app/
│   │   ├── api/routes/      # FastAPI endpoints
│   │   ├── core/            # Config, database, security
│   │   ├── models/          # SQLAlchemy ORM models
│   │   ├── providers/       # AI provider adapters
│   │   ├── schemas/         # Pydantic request/response models
│   │   ├── services/        # Business logic
│   │   ├── utils/           # Utilities (FFmpeg, timestamps, etc.)
│   │   ├── workers/         # Background processing
│   │   └── main.py          # FastAPI application
│   ├── media/               # Uploaded & processed media
│   ├── tests/               # Automated tests
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── app/             # Next.js App Router pages
│   │   ├── components/      # React components
│   │   ├── hooks/           # Custom hooks
│   │   ├── lib/             # API client, utilities
│   │   ├── store/           # Zustand state management
│   │   └── types/           # TypeScript types
│   ├── package.json
│   └── tailwind.config.ts
├── docs/
└── README.md
```

## Auto-Dubbing Pipeline (16 Phases)

1. Import & validate media
2. Extract original audio
3. Detect language & speech
4. Perform speaker diarization
5. Generate transcription
6. Review & normalize segments
7. Translate dialogue
8. Assign speaker voices
9. Generate AI speech (Microsoft Azure)
10. Optimize dialogue duration (Auto-Fit)
11. Synchronize audio
12. Generate subtitles
13. Mix audio tracks
14. Render final video
15. Validate output
16. Save & present export

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | JWT signing key | Yes |
| `AZURE_SPEECH_KEY` | Azure Speech API key | For TTS |
| `AZURE_SPEECH_REGION` | Azure Speech region | For TTS |
| `GEMINI_API_KEY` | Google Gemini API key | For ASR/Translation |
| `DATABASE_URL` | SQLite connection string | No (default provided) |
| `MAX_UPLOAD_SIZE_MB` | Max upload size in MB | No (default: 2048) |

## License

Proprietary — AI DUBBER PRO

## Version History

- **v2.1.0** — Microsoft Azure Khmer Neural TTS (Sreymom + Piseth)
- **v2.0.0** — Initial release
