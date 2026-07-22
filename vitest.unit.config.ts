import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    include: [
      'apps/**/*.test.ts',
      'apps/**/*.test.tsx',
      'packages/**/*.test.ts',
      'packages/**/*.test.tsx',
      'tools/catalogue/**/*.test.ts',
    ],
    passWithNoTests: false,
    restoreMocks: true,
  },
});
