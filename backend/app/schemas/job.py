"""Job schemas."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JobCreate(BaseModel):
    project_id: str
    task_type: str
    priority: int = 5
    parameters: Optional[dict] = None


class JobResponse(BaseModel):
    id: str
    project_id: str
    task_type: str
    status: str
    priority: int
    current_phase: Optional[str] = None
    phase_number: int
    total_phases: int
    progress_percent: float
    progress_message: Optional[str] = None
    parameters: Optional[dict] = None
    result: Optional[dict] = None
    error_message: Optional[str] = None
    retry_count: int
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
