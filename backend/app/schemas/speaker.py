"""Speaker schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SpeakerResponse(BaseModel):
    id: str
    project_id: str
    display_name: str
    speaker_label: str
    voice_presentation: Optional[str] = None
    assigned_voice_id: Optional[str] = None
    assigned_voice_name: Optional[str] = None
    voice_settings: Optional[dict] = None
    confidence: Optional[float] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class SpeakerUpdate(BaseModel):
    display_name: Optional[str] = None
    voice_presentation: Optional[str] = None
    assigned_voice_id: Optional[str] = None
    assigned_voice_name: Optional[str] = None
    voice_settings: Optional[dict] = None


class SpeakerAssignVoice(BaseModel):
    speaker_id: str
    voice_id: str
    voice_name: Optional[str] = None
    voice_settings: Optional[dict] = None
