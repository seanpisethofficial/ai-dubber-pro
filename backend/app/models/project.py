"""Project model."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON

from app.core.database import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        String(50), default="created", nullable=False, index=True
    )  # created, processing, transcribed, translated, dubbed, exported, error
    source_language: Mapped[str | None] = mapped_column(String(10), nullable=True)
    target_language: Mapped[str] = mapped_column(String(10), default="km", nullable=False)
    translation_mode: Mapped[str] = mapped_column(
        String(50), default="natural", nullable=False
    )  # natural, cinematic, casual, formal, literal
    auto_fit_mode: Mapped[str] = mapped_column(
        String(50), default="balanced", nullable=False
    )  # balanced, strict, relaxed, none
    context_memory: Mapped[dict | None] = mapped_column(JSON, nullable=True, default=dict)
    export_settings: Mapped[dict | None] = mapped_column(JSON, nullable=True, default=dict)
    owner_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
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
    owner = relationship("User", back_populates="projects")
    media_files = relationship("MediaFile", back_populates="project", cascade="all, delete-orphan")
    transcript_segments = relationship(
        "TranscriptSegment", back_populates="project", cascade="all, delete-orphan"
    )
    speakers = relationship("Speaker", back_populates="project", cascade="all, delete-orphan")
    translation_segments = relationship(
        "TranslationSegment", back_populates="project", cascade="all, delete-orphan"
    )
    generated_audios = relationship(
        "GeneratedAudio", back_populates="project", cascade="all, delete-orphan"
    )
    subtitles = relationship("Subtitle", back_populates="project", cascade="all, delete-orphan")
    jobs = relationship("Job", back_populates="project", cascade="all, delete-orphan")
