"""Pydantic v2 schemas for AI DUBBER PRO."""

from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse, UserResponse
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectResponse
from app.schemas.media import MediaUploadResponse, MediaAnalysis
from app.schemas.transcription import TranscriptionRequest, TranscriptSegmentResponse
from app.schemas.translation import TranslationRequest, TranslationResponse
from app.schemas.tts import TTSGenerateRequest, TTSPreviewRequest, VoiceInfo, TTSResponse
from app.schemas.speaker import SpeakerResponse, SpeakerUpdate
from app.schemas.subtitle import SubtitleCreate, SubtitleUpdate, SubtitleResponse, SRTExport
from app.schemas.export import ExportRequest, ExportResponse
from app.schemas.job import JobResponse, JobCreate
