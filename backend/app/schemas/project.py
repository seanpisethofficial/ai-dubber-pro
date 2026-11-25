"""Project schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    source_language: Optional[str] = None
    target_language: str = "km"
    translation_mode: str = "natural"
    auto_fit_mode: str = "balanced"
    export_settings: Optional[dict] = None


class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[str] = None
    source_language: Optional[str] = None
    target_language: Optional[str] = None
    translation_mode: Optional[str] = None
    auto_fit_mode: Optional[str] = None
    context_memory: Optional[dict] = None
    export_settings: Optional[dict] = None


class ProjectResponse(BaseModel):
    id: str
    name: str
    description: Optional[str] = None
    status: str
    source_language: Optional[str] = None
    target_language: str
    translation_mode: str
    auto_fit_mode: str
    context_memory: Optional[dict] = None
    export_settings: Optional[dict] = None
    owner_id: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
