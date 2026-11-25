"""Subtitle schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SubtitleCreate(BaseModel):
    start_time: float = Field(..., ge=0)
    end_time: float = Field(..., ge=0)
    text: str = Field(..., min_length=1)
    language: str = "km"
    speaker_label: Optional[str] = None
    style: Optional[dict] = None
    subtitle_index: int = 0


class SubtitleUpdate(BaseModel):
    start_time: Optional[float] = Field(None, ge=0)
    end_time: Optional[float] = Field(None, ge=0)
    text: Optional[str] = None
    language: Optional[str] = None
    speaker_label: Optional[str] = None
    style: Optional[dict] = None


class SubtitleResponse(BaseModel):
    id: str
    project_id: str
    start_time: float
    end_time: float
    text: str
    language: str
    speaker_label: Optional[str] = None
    style: Optional[dict] = None
    subtitle_index: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class SRTExport(BaseModel):
    project_id: str
    content: str
    filename: str
    total_subtitles: int
