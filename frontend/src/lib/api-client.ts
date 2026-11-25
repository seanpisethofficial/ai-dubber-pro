import api, { API_BASE_URL } from './api';
import type {
  Project,
  MediaFile,
  TranscriptSegment,
  TranslationSegment,
  Speaker,
  VoiceProfile,
  GeneratedAudio,
  Subtitle,
  Job,
  ProviderConfig,
  ExportPreset,
  HealthStatus,
  CreateProjectRequest,
  TTSRequest,
  TTSPreviewRequest,
  TranscriptionRequest,
  TranslationRequest,
  ExportRequest,
  ExportSettings,
  UploadProgress,
} from '@/types';

// ============================================================
// Auth
// ============================================================
export const authApi = {
  register: async (data: { username: string; email: string; password: string }) => {
    const res = await api.post('/auth/register', data);
    return res.data;
  },
  login: async (data: { username: string; password: string }) => {
    const formData = new URLSearchParams();
    formData.append('username', data.username);
    formData.append('password', data.password);
    const res = await api.post('/auth/login', formData, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
    if (res.data.access_token) {
      localStorage.setItem('auth_token', res.data.access_token);
    }
    return res.data;
  },
  getMe: async () => {
    const res = await api.get('/auth/me');
    return res.data;
  },
};

// ============================================================
// Projects
// ============================================================
export const projectsApi = {
  create: async (data: CreateProjectRequest): Promise<Project> => {
    const res = await api.post('/projects', data);
    return res.data;
  },
  list: async (): Promise<Project[]> => {
    const res = await api.get('/projects');
    return res.data;
  },
  get: async (id: string): Promise<Project> => {
    const res = await api.get(`/projects/${id}`);
    return res.data;
  },
  update: async (id: string, data: Partial<CreateProjectRequest>): Promise<Project> => {
    const res = await api.put(`/projects/${id}`, data);
    return res.data;
  },
  delete: async (id: string): Promise<void> => {
    await api.delete(`/projects/${id}`);
  },
};

// ============================================================
// Media
// ============================================================
export const mediaApi = {
  upload: async (
    projectId: string,
    file: File,
    onProgress?: (progress: UploadProgress) => void
  ): Promise<MediaFile> => {
    const formData = new FormData();
    formData.append('file', file);
    const res = await api.post(`/projects/${projectId}/media/upload`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
      timeout: 600000,
      onUploadProgress: (event) => {
        if (onProgress && event.total) {
          onProgress({
            loaded: event.loaded,
            total: event.total,
            percentage: Math.round((event.loaded * 100) / event.total),
          });
        }
      },
    });
    return res.data;
  },
  extractAudio: async (projectId: string): Promise<{ audio_path: string }> => {
    const res = await api.post(`/projects/${projectId}/media/extract-audio`);
    return res.data;
  },
  listFiles: async (projectId: string): Promise<MediaFile[]> => {
    const res = await api.get(`/projects/${projectId}/media`);
    return res.data;
  },
};

// ============================================================
// Transcription
// ============================================================
export const transcriptionApi = {
  transcribe: async (data: TranscriptionRequest): Promise<Job> => {
    const res = await api.post(`/projects/${data.project_id}/transcription/transcribe`, data);
    return res.data;
  },
  getSegments: async (projectId: string): Promise<TranscriptSegment[]> => {
    const res = await api.get(`/projects/${projectId}/transcription/segments`);
    return res.data;
  },
  updateSegment: async (
    projectId: string,
    segmentId: string,
    data: Partial<TranscriptSegment>
  ): Promise<TranscriptSegment> => {
    const res = await api.put(
      `/projects/${projectId}/transcription/segments/${segmentId}`,
      data
    );
    return res.data;
  },
};

// ============================================================
// Translation
// ============================================================
export const translationApi = {
  translate: async (data: TranslationRequest): Promise<Job> => {
    const res = await api.post(`/projects/${data.project_id}/translation/translate`, data);
    return res.data;
  },
  getSegments: async (projectId: string): Promise<TranslationSegment[]> => {
    const res = await api.get(`/projects/${projectId}/translation/segments`);
    return res.data;
  },
  updateSegment: async (
    projectId: string,
    segmentId: string,
    data: Partial<TranslationSegment>
  ): Promise<TranslationSegment> => {
    const res = await api.put(
      `/projects/${projectId}/translation/segments/${segmentId}`,
      data
    );
    return res.data;
  },
  translateSingle: async (
    projectId: string,
    data: { text: string; source_language: string; target_language: string; mode?: string }
  ): Promise<{ translated_text: string }> => {
    const res = await api.post(`/projects/${projectId}/translation/translate-single`, data);
    return res.data;
  },
};

// ============================================================
// TTS (Text-to-Speech)
// ============================================================
export const ttsApi = {
  generate: async (data: TTSRequest): Promise<GeneratedAudio> => {
    const res = await api.post('/tts/generate', data);
    return res.data;
  },
  preview: async (data: TTSPreviewRequest): Promise<Blob> => {
    const res = await api.post('/tts/preview', data, { responseType: 'blob' });
    return res.data;
  },
  getVoices: async (): Promise<VoiceProfile[]> => {
    const res = await api.get('/tts/voices');
    return res.data;
  },
  health: async (): Promise<{ status: string; provider: string }> => {
    const res = await api.get('/tts/health');
    return res.data;
  },
  testConnection: async (): Promise<{ success: boolean; message: string }> => {
    const res = await api.post('/tts/test-connection');
    return res.data;
  },
  deleteAudio: async (audioId: string): Promise<void> => {
    await api.delete(`/tts/audio/${audioId}`);
  },
};

// ============================================================
// Speakers
// ============================================================
export const speakersApi = {
  list: async (projectId: string): Promise<Speaker[]> => {
    const res = await api.get(`/projects/${projectId}/speakers`);
    return res.data;
  },
  assignVoice: async (
    projectId: string,
    speakerId: string,
    data: { voice_id: string; voice_name: string }
  ): Promise<Speaker> => {
    const res = await api.put(
      `/projects/${projectId}/speakers/${speakerId}/voice`,
      data
    );
    return res.data;
  },
  update: async (
    projectId: string,
    speakerId: string,
    data: Partial<Speaker>
  ): Promise<Speaker> => {
    const res = await api.put(`/projects/${projectId}/speakers/${speakerId}`, data);
    return res.data;
  },
};

// ============================================================
// Subtitles
// ============================================================
export const subtitlesApi = {
  list: async (projectId: string): Promise<Subtitle[]> => {
    const res = await api.get(`/projects/${projectId}/subtitles`);
    return res.data;
  },
  generate: async (projectId: string): Promise<Job> => {
    const res = await api.post(`/projects/${projectId}/subtitles/generate`);
    return res.data;
  },
  importSrt: async (projectId: string, file: File): Promise<Subtitle[]> => {
    const formData = new FormData();
    formData.append('file', file);
    const res = await api.post(`/projects/${projectId}/subtitles/import`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    return res.data;
  },
  exportSrt: async (projectId: string): Promise<Blob> => {
    const res = await api.get(`/projects/${projectId}/subtitles/export/srt`, {
      responseType: 'blob',
    });
    return res.data;
  },
  exportVtt: async (projectId: string): Promise<Blob> => {
    const res = await api.get(`/projects/${projectId}/subtitles/export/vtt`, {
      responseType: 'blob',
    });
    return res.data;
  },
  update: async (
    projectId: string,
    subtitleId: string,
    data: Partial<Subtitle>
  ): Promise<Subtitle> => {
    const res = await api.put(
      `/projects/${projectId}/subtitles/${subtitleId}`,
      data
    );
    return res.data;
  },
};

// ============================================================
// Export
// ============================================================
export const exportApi = {
  render: async (data: ExportRequest): Promise<Job> => {
    const res = await api.post('/export/render', data);
    return res.data;
  },
  getStatus: async (jobId: string): Promise<Job> => {
    const res = await api.get(`/export/status/${jobId}`);
    return res.data;
  },
  download: async (jobId: string): Promise<Blob> => {
    const res = await api.get(`/export/download/${jobId}`, { responseType: 'blob' });
    return res.data;
  },
  getPresets: async (): Promise<ExportPreset[]> => {
    const res = await api.get('/export/presets');
    return res.data;
  },
};

// ============================================================
// Providers
// ============================================================
export const providersApi = {
  list: async (): Promise<ProviderConfig[]> => {
    const res = await api.get('/providers');
    return res.data;
  },
  configure: async (data: Partial<ProviderConfig>): Promise<ProviderConfig> => {
    const res = await api.post('/providers', data);
    return res.data;
  },
  update: async (id: string, data: Partial<ProviderConfig>): Promise<ProviderConfig> => {
    const res = await api.put(`/providers/${id}`, data);
    return res.data;
  },
  remove: async (id: string): Promise<void> => {
    await api.delete(`/providers/${id}`);
  },
  test: async (id: string): Promise<{ success: boolean; message: string }> => {
    const res = await api.post(`/providers/${id}/test`);
    return res.data;
  },
  getStatus: async (): Promise<{ providers: ProviderConfig[] }> => {
    const res = await api.get('/providers/status');
    return res.data;
  },
};

// ============================================================
// Jobs
// ============================================================
export const jobsApi = {
  list: async (projectId?: string): Promise<Job[]> => {
    const params = projectId ? { project_id: projectId } : {};
    const res = await api.get('/jobs', { params });
    return res.data;
  },
  get: async (jobId: string): Promise<Job> => {
    const res = await api.get(`/jobs/${jobId}`);
    return res.data;
  },
  cancel: async (jobId: string): Promise<void> => {
    await api.post(`/jobs/${jobId}/cancel`);
  },
  getProgress: async (jobId: string): Promise<{ progress: number; phase: string; status: string }> => {
    const res = await api.get(`/jobs/${jobId}/progress`);
    return res.data;
  },
};

// ============================================================
// Health
// ============================================================
export const healthApi = {
  check: async (): Promise<HealthStatus> => {
    const res = await api.get('/health');
    return res.data;
  },
};

// ============================================================
// Auto Dubbing
// ============================================================
export const dubbingApi = {
  startAutoDubbing: async (projectId: string): Promise<Job> => {
    const res = await api.post(`/projects/${projectId}/dubbing/start`);
    return res.data;
  },
  getProgress: async (projectId: string): Promise<Job> => {
    const res = await api.get(`/projects/${projectId}/dubbing/progress`);
    return res.data;
  },
};
