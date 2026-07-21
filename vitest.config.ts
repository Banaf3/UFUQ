import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    include: ['apps/**/*.test.ts', 'packages/**/*.test.ts', 'tools/**/*.test.ts'],
    passWithNoTests: false,
    restoreMocks: true,
  },
});
