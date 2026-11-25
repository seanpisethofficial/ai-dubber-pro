"""VoiceProfile and GeneratedAudio models."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class VoiceProfile(Base):
    __tablename__ = "voice_profiles"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    voice_id: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    display_name: Mapped[str] = mapped_column(String(255), nullable=False)
    provider: Mapped[str] = mapped_column(String(50), nullable=False)  # microsoft_azure
    language: Mapped[str] = mapped_column(String(10), nullable=False)
    locale: Mapped[str] = mapped_column(String(20), nullable=False)
    gender: Mapped[str] = mapped_column(String(20), nullable=False)  # Male, Female
    voice_type: Mapped[str] = mapped_column(String(50), default="Neural", nullable=False)
    supports_ssml: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    supports_prosody: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    supports_emotions: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    default_settings: Mapped[dict | None] = mapped_column(JSON, nullable=True, default=dict)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )

    # Relationships
    generated_audios = relationship("GeneratedAudio", back_populates="voice_profile")


class GeneratedAudio(Base):
    __tablename__ = "generated_audios"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4())
    )
    project_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True
    )
    transcript_segment_id: Mapped[str | None] = mapped_column(
        String(36),
        ForeignKey("transcript_segments.id", ondelete="SET NULL"),
        nullable=True,
    )
    speaker_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("speakers.id", ondelete="SET NULL"), nullable=True
    )
    voice_id: Mapped[str | None] = mapped_column(
        String(255), ForeignKey("voice_profiles.voice_id", ondelete="SET NULL"), nullable=True
    )
    text: Mapped[str] = mapped_column(Text, nullable=False)
    file_path: Mapped[str | None] = mapped_column(Text, nullable=True)
    duration: Mapped[float | None] = mapped_column(Float, nullable=True)  # target duration
    target_duration: Mapped[float | None] = mapped_column(Float, nullable=True)
    actual_duration: Mapped[float | None] = mapped_column(Float, nullable=True)
    speed_factor: Mapped[float] = mapped_column(Float, default=1.0, nullable=False)
    fit_status: Mapped[str | None] = mapped_column(
        String(20), nullable=True
    )  # fitted, over, under, skipped
    status: Mapped[str] = mapped_column(
        String(20), default="pending", nullable=False
    )  # pending, generating, completed, failed
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False
    )

    # Relationships
    project = relationship("Project", back_populates="generated_audios")
    transcript_segment = relationship("TranscriptSegment", back_populates="generated_audios")
    speaker = relationship("Speaker")
    voice_profile = relationship("VoiceProfile", back_populates="generated_audios")
