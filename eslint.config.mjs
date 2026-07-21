import js from '@eslint/js';
import reactHooks from 'eslint-plugin-react-hooks';
import reactRefresh from 'eslint-plugin-react-refresh';
import tseslint from 'typescript-eslint';

const typescriptFiles = ['**/*.{ts,tsx}'];

export default tseslint.config(
  {
    ignores: [
      '**/node_modules/**',
      '**/dist/**',
      '**/dist-types/**',
      'coverage/**',
      'playwright-report/**',
      'test-results/**',
      'local-reference/**',
    ],
  },
  { ...js.configs.recommended, files: typescriptFiles },
  ...tseslint.configs.recommended.map((config) => ({ ...config, files: typescriptFiles })),
  {
    files: [
      'packages/{astronomy-core,assessment-core,bkt-core,adaptive-policy,tutoring-core}/src/**/*.{ts,tsx}',
    ],
    rules: {
      'no-restricted-imports': [
        'error',
        {
          patterns: [
            {
              group: [
                'react',
                'react/*',
                'three',
                'three/*',
                '@react-three/fiber',
                'express',
                'express/*',
                'mysql',
                'mysql2',
                'mysql2/*',
                '@ufuq/web',
                '@ufuq/api',
              ],
              message:
                'Pure domain packages cannot import application, framework, or database code.',
            },
          ],
        },
      ],
    },
  },
  {
    files: ['packages/contracts/src/**/*.{ts,tsx}'],
    rules: {
      'no-restricted-imports': ['error', { patterns: ['*'] }],
    },
  },
  {
    files: ['apps/web/src/**/*.{ts,tsx}'],
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': ['warn', { allowConstantExport: true }],
    },
  },
);
