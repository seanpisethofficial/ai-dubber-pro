"""Translation schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TranslationRequest(BaseModel):
    source_language: Optional[str] = None  # auto-detect if None
    target_language: str = "km"
    translation_mode: str = "natural"
    provider: str = "gemini"
    context_memory: Optional[dict] = None


class TranslationSingleRequest(BaseModel):
    text: str
    source_language: Optional[str] = None
    target_language: str = "km"
    translation_mode: str = "natural"
    context: Optional[str] = None


class TranslationSegmentResponse(BaseModel):
    id: str
    project_id: str
    transcript_segment_id: str
    source_text: str
    translated_text: str
    source_language: str
    target_language: str
    translation_mode: str
    confidence: Optional[float] = None
    quality_warnings: Optional[dict] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class TranslationResponse(BaseModel):
    project_id: str
    total_segments: int
    translated_segments: int
    target_language: str
    translation_mode: str
    segments: list[TranslationSegmentResponse] = []
