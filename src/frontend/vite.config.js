import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    host: true,
    port: 3000
  },
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: '/src/__tests__/setupTests.jsx'
  },
  plugins: [react()]
})
