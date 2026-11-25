"""Application configuration using pydantic-settings."""

from pathlib import Path
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """AI DUBBER PRO v2.1.0 configuration."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    APP_NAME: str = "AI DUBBER PRO"
    APP_VERSION: str = "2.1.0"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Security
    SECRET_KEY: str = "change-this-to-a-random-secret"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440  # 24 hours
    ALGORITHM: str = "HS256"

    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./ai_dubber_pro.db"

    # Microsoft Azure Speech (TTS)
    AZURE_SPEECH_KEY: Optional[str] = None
    AZURE_SPEECH_REGION: Optional[str] = None

    # Google Gemini (Translation & ASR only)
    GEMINI_API_KEY: Optional[str] = None

    # Media paths (relative to project root)
    MEDIA_ROOT: str = "media"
    UPLOAD_DIR: str = "media/uploads"
    PROCESSED_DIR: str = "media/processed"
    EXPORT_DIR: str = "media/exports"
    TEMP_DIR: str = "media/temp"

    # Upload limits
    MAX_UPLOAD_SIZE_MB: int = 2048  # 2GB
    ALLOWED_VIDEO_EXTENSIONS: list[str] = [".mp4", ".mkv", ".avi", ".mov", ".webm", ".flv"]
    ALLOWED_AUDIO_EXTENSIONS: list[str] = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"]
    ALLOWED_SUBTITLE_EXTENSIONS: list[str] = [".srt", ".vtt", ".ass", ".ssa"]

    # FFmpeg
    FFMPEG_PATH: str = "ffmpeg"
    FFPROBE_PATH: str = "ffprobe"

    # TTS defaults
    TTS_DEFAULT_SAMPLE_RATE: int = 16000
    TTS_DEFAULT_FORMAT: str = "wav"

    # Auto-fit settings
    AUTOFIT_MIN_SPEED: float = 0.75
    AUTOFIT_MAX_SPEED: float = 1.5
    AUTOFIT_TOLERANCE: float = 0.1  # 100ms tolerance

    @property
    def max_upload_bytes(self) -> int:
        return self.MAX_UPLOAD_SIZE_MB * 1024 * 1024

    def get_media_path(self, subdir: str) -> Path:
        return Path(self.MEDIA_ROOT) / subdir

    def ensure_media_dirs(self) -> None:
        """Create all media directories if they don't exist."""
        for d in [self.UPLOAD_DIR, self.PROCESSED_DIR, self.EXPORT_DIR, self.TEMP_DIR]:
            Path(d).mkdir(parents=True, exist_ok=True)


settings = Settings()
