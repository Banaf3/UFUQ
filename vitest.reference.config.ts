import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    include: ['tests/reference/**/*.test.ts'],
    passWithNoTests: false,
    restoreMocks: true,
  },
});
