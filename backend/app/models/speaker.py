"""Speaker model."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, Float, ForeignKey, String, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Speaker(Base):
    __tablename__ = "speakers"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    project_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True
    )
    display_name: Mapped[str] = mapped_column(String(100), nullable=False)
    speaker_label: Mapped[str] = mapped_column(String(50), nullable=False)  # SPEAKER_00, etc.
    voice_presentation: Mapped[str | None] = mapped_column(
        String(20), nullable=True
    )  # male, female, neutral
    assigned_voice_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    assigned_voice_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    voice_settings: Mapped[dict | None] = mapped_column(JSON, nullable=True, default=dict)
    embedding: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    confidence: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # Relationships
    project = relationship("Project", back_populates="speakers")
    transcript_segments = relationship("TranscriptSegment", back_populates="speaker")
