"""Transcription schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TranscriptionRequest(BaseModel):
    language: Optional[str] = None  # auto-detect if None
    provider: str = "gemini"
    enable_diarization: bool = False
    max_speakers: int = Field(default=10, ge=1, le=50)


class TranscriptSegmentResponse(BaseModel):
    id: str
    project_id: str
    speaker_id: Optional[str] = None
    start_time: float
    end_time: float
    original_text: str
    language: Optional[str] = None
    confidence: Optional[float] = None
    word_timestamps: Optional[dict] = None
    segment_index: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class TranscriptSegmentUpdate(BaseModel):
    original_text: Optional[str] = None
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    speaker_id: Optional[str] = None
    language: Optional[str] = None
