"""TTS schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TTSGenerateRequest(BaseModel):
    project_id: str
    segment_ids: Optional[list[str]] = None  # None = all segments
    voice_id: Optional[str] = None  # Override per-speaker assignment
    rate: str = "0%"
    pitch: str = "0%"
    volume: str = "100%"
    auto_fit: bool = True


class TTSPreviewRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000)
    voice_id: str
    rate: str = "0%"
    pitch: str = "0%"
    volume: str = "100%"


class VoiceInfo(BaseModel):
    voice_id: str
    display_name: str
    provider: str
    language: str
    locale: str
    gender: str
    voice_type: str
    supports_ssml: bool = True
    supports_prosody: bool = True
    supports_emotions: bool = False


class TTSResponse(BaseModel):
    id: str
    project_id: str
    text: str
    voice_id: Optional[str] = None
    file_path: Optional[str] = None
    duration: Optional[float] = None
    target_duration: Optional[float] = None
    actual_duration: Optional[float] = None
    speed_factor: float = 1.0
    fit_status: Optional[str] = None
    status: str
    error_message: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}
