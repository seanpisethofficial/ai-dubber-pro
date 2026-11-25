import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'AI DUBBER PRO v2.1.0 - Intelligent Voice. Perfect Synchronization.',
  description: 'Professional AI-powered video dubbing studio with Microsoft Khmer voice synthesis, real-time translation, and intelligent synchronization.',
  keywords: ['AI dubbing', 'video translation', 'Khmer voice', 'TTS', 'speech synthesis'],
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
      </head>
      <body className="min-h-screen bg-brand-bg text-brand-text-primary">
        {children}
      </body>
    </html>
  );
}
