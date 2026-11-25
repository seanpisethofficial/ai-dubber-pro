import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          bg: '#0f0f1a',
          charcoal: '#1a1a2e',
          surface: '#16213e',
          card: '#1e1e36',
          border: '#2d2d4a',
          'text-primary': '#e2e8f0',
          'text-secondary': '#94a3b8',
          purple: '#7c3aed',
          'purple-hover': '#8b5cf6',
          blue: '#3b82f6',
          'blue-hover': '#60a5fa',
          success: '#22c55e',
          error: '#ef4444',
          warning: '#eab308',
        },
      },
      fontFamily: {
        sans: ['Inter', 'Noto Sans Khmer', 'system-ui', 'sans-serif'],
        khmer: ['Noto Sans Khmer', 'sans-serif'],
      },
      animation: {
        'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'slide-in': 'slideIn 0.3s ease-out',
        'fade-in': 'fadeIn 0.2s ease-out',
      },
      keyframes: {
        slideIn: {
          '0%': { transform: 'translateX(-100%)', opacity: '0' },
          '100%': { transform: 'translateX(0)', opacity: '1' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
};

export default config;
