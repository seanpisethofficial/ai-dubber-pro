"""Export schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ExportRequest(BaseModel):
    resolution: Optional[str] = None  # e.g. "1920x1080", None = match source
    video_codec: str = "libx264"
    audio_codec: str = "aac"
    video_bitrate: Optional[str] = None  # e.g. "5000k"
    audio_bitrate: str = "192k"
    format: str = "mp4"
    burn_subtitles: bool = False
    subtitle_language: str = "km"
    include_original_audio: bool = False
    original_audio_volume: float = Field(default=0.1, ge=0.0, le=1.0)
    dubbed_audio_volume: float = Field(default=1.0, ge=0.0, le=1.0)


class ExportResponse(BaseModel):
    job_id: str
    project_id: str
    status: str
    file_path: Optional[str] = None
    file_size: Optional[int] = None
    duration: Optional[float] = None
    format: str = "mp4"
    created_at: datetime

    model_config = {"from_attributes": True}
