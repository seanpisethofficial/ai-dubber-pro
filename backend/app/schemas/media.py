"""Media schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MediaAnalysis(BaseModel):
    duration: Optional[float] = None
    width: Optional[int] = None
    height: Optional[int] = None
    fps: Optional[float] = None
    video_codec: Optional[str] = None
    audio_codec: Optional[str] = None
    audio_channels: Optional[int] = None
    audio_sample_rate: Optional[int] = None
    file_size: int = 0
    mime_type: Optional[str] = None
    file_type: str = "video"


class MediaUploadResponse(BaseModel):
    id: str
    project_id: str
    filename: str
    file_path: str
    file_size: int
    mime_type: Optional[str] = None
    file_type: str
    duration: Optional[float] = None
    width: Optional[int] = None
    height: Optional[int] = None
    fps: Optional[float] = None
    video_codec: Optional[str] = None
    audio_codec: Optional[str] = None
    extracted_audio_path: Optional[str] = None
    created_at: datetime

    model_config = {"from_attributes": True}
