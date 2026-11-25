// ============================================================
// AI DUBBER PRO v2.1.0 - Type Definitions
// ============================================================

// === Enums ===
export enum ProcessingStatus {
  IDLE = 'idle',
  PENDING = 'pending',
  PROCESSING = 'processing',
  COMPLETED = 'completed',
  FAILED = 'failed',
  CANCELLED = 'cancelled',
}

export enum TranslationMode {
  ADAPTIVE = 'adaptive',
  PRECISE = 'precise',
  CREATIVE = 'creative',
}

export enum AutoFitMode {
  SPEED_ADJUST = 'speed_adjust',
  TRIM_SILENCE = 'trim_silence',
  BOTH = 'both',
  NONE = 'none',
}

export enum ExportFormat {
  MP4 = 'mp4',
  MKV = 'mkv',
  AVI = 'avi',
  MOV = 'mov',
  WEBM = 'webm',
}

export enum SubtitleFormat {
  SRT = 'srt',
  VTT = 'vtt',
  ASS = 'ass',
}

export enum DubbingPhase {
  INIT = 'initialization',
  UPLOAD = 'media_upload',
  EXTRACT = 'audio_extraction',
  TRANSCRIBE = 'transcription',
  SPEAKER_DETECT = 'speaker_detection',
  TRANSLATE = 'translation',
  VOICE_ASSIGN = 'voice_assignment',
  TTS_GENERATE = 'tts_generation',
  TIMING_ADJUST = 'timing_adjustment',
  AUDIO_MIX = 'audio_mixing',
  SUBTITLE_GEN = 'subtitle_generation',
  VIDEO_RENDER = 'video_rendering',
  QUALITY_CHECK = 'quality_check',
  FINALIZE = 'finalization',
  EXPORT = 'export',
  COMPLETE = 'complete',
}

// === Core Models ===
export interface Project {
  id: string;
  name: string;
  description: string;
  source_language: string;
  target_language: string;
  translation_mode: TranslationMode;
  auto_fit_mode: AutoFitMode;
  status: ProcessingStatus;
  progress: number;
  current_phase: DubbingPhase | null;
  media_file: MediaFile | null;
  created_at: string;
  updated_at: string;
  output_path: string | null;
}

export interface MediaFile {
  id: string;
  project_id: string;
  filename: string;
  original_filename: string;
  file_path: string;
  file_size: number;
  mime_type: string;
  duration: number;
  width: number;
  height: number;
  fps: number;
  codec: string;
  audio_extracted: boolean;
  audio_path: string | null;
  created_at: string;
}

export interface TranscriptSegment {
  id: string;
  project_id: string;
  segment_index: number;
  speaker: string;
  text: string;
  start_time: number;
  end_time: number;
  confidence: number;
  language: string;
  word_timestamps: WordTimestamp[];
}

export interface WordTimestamp {
  word: string;
  start: number;
  end: number;
  confidence: number;
}

export interface TranslationSegment {
  id: string;
  project_id: string;
  segment_index: number;
  original_text: string;
  translated_text: string;
  source_language: string;
  target_language: string;
  start_time: number;
  end_time: number;
  speaker: string;
  quality_score: number;
  warnings: string[];
  translation_mode: TranslationMode;
}

export interface Speaker {
  id: string;
  project_id: string;
  speaker_label: string;
  display_name: string;
  gender: 'male' | 'female' | 'unknown';
  voice_id: string | null;
  voice_name: string | null;
  segment_count: number;
  total_duration: number;
  color: string;
}

export interface VoiceProfile {
  id: string;
  name: string;
  display_name: string;
  short_name: string;
  gender: 'Male' | 'Female';
  locale: string;
  language: string;
  voice_type: string;
  sample_rate: number;
  provider: string;
  is_neural: boolean;
}

export interface GeneratedAudio {
  id: string;
  project_id: string;
  segment_index: number;
  voice_id: string;
  voice_name: string;
  text: string;
  file_path: string;
  duration: number;
  original_duration: number;
  rate: string;
  pitch: string;
  volume: string;
  created_at: string;
}

export interface Subtitle {
  id: string;
  project_id: string;
  segment_index: number;
  text: string;
  start_time: number;
  end_time: number;
  speaker: string;
  style: SubtitleStyle;
}

export interface SubtitleStyle {
  font_size: number;
  font_color: string;
  background_color: string;
  position: 'top' | 'center' | 'bottom';
  alignment: 'left' | 'center' | 'right';
}

export interface Job {
  id: string;
  project_id: string;
  job_type: string;
  status: ProcessingStatus;
  progress: number;
  current_phase: string | null;
  phases: PhaseStatus[];
  result: any;
  error: string | null;
  created_at: string;
  updated_at: string;
  completed_at: string | null;
}

export interface PhaseStatus {
  phase: DubbingPhase;
  status: ProcessingStatus;
  progress: number;
  message: string;
  started_at: string | null;
  completed_at: string | null;
}

export interface ProviderConfig {
  id: string;
  provider_type: 'azure_speech' | 'google_gemini';
  display_name: string;
  api_key: string;
  region?: string;
  model?: string;
  is_configured: boolean;
  is_active: boolean;
  last_tested: string | null;
  test_result: boolean | null;
}

export interface ExportSettings {
  format: ExportFormat;
  resolution: string;
  video_codec: string;
  video_bitrate: string;
  audio_codec: string;
  audio_bitrate: string;
  frame_rate: number;
  burn_subtitles: boolean;
  subtitle_format: SubtitleFormat;
  include_original_audio: boolean;
  original_audio_volume: number;
  dubbed_audio_volume: number;
}

export interface ExportPreset {
  id: string;
  name: string;
  description: string;
  icon: string;
  settings: ExportSettings;
}

// === API Response Types ===
export interface ApiResponse<T> {
  data: T;
  message: string;
  success: boolean;
}

export interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  page_size: number;
  total_pages: number;
}

export interface HealthStatus {
  status: string;
  version: string;
  ffmpeg_available: boolean;
  azure_configured: boolean;
  gemini_configured: boolean;
  uptime: number;
}

export interface UploadProgress {
  loaded: number;
  total: number;
  percentage: number;
}

export interface TTSRequest {
  text: string;
  voice_id: string;
  rate?: string;
  pitch?: string;
  volume?: string;
  project_id?: string;
  segment_index?: number;
}

export interface TTSPreviewRequest {
  text: string;
  voice_id: string;
  rate?: string;
  pitch?: string;
  volume?: string;
}

export interface TranscriptionRequest {
  project_id: string;
  language?: string;
  model?: string;
}

export interface TranslationRequest {
  project_id: string;
  source_language: string;
  target_language: string;
  mode?: TranslationMode;
}

export interface ExportRequest {
  project_id: string;
  settings: ExportSettings;
}

export interface CreateProjectRequest {
  name: string;
  description?: string;
  source_language: string;
  target_language: string;
  translation_mode?: TranslationMode;
  auto_fit_mode?: AutoFitMode;
}

// === View Types ===
export type StudioView =
  | 'dashboard'
  | 'dubbing'
  | 'speakers'
  | 'translation'
  | 'voice'
  | 'subtitles'
  | 'timeline'
  | 'export';

export interface TimelineTrackData {
  id: string;
  label: string;
  type: 'video' | 'audio' | 'dubbed' | 'subtitle';
  segments: TimelineSegmentData[];
  color: string;
  muted: boolean;
  locked: boolean;
}

export interface TimelineSegmentData {
  id: string;
  trackId: string;
  startTime: number;
  endTime: number;
  label: string;
  color: string;
  data: any;
}
