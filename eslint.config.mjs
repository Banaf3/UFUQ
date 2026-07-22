import js from '@eslint/js';
import reactHooks from 'eslint-plugin-react-hooks';
import reactRefresh from 'eslint-plugin-react-refresh';
import tseslint from 'typescript-eslint';

const typescriptFiles = ['**/*.{ts,tsx}'];
const nodeJavaScriptFiles = ['scripts/**/*.mjs', '*.config.mjs'];

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
  {
    ...js.configs.recommended,
    files: nodeJavaScriptFiles,
    languageOptions: {
      globals: {
        AggregateError: 'readonly',
        clearTimeout: 'readonly',
        console: 'readonly',
        fetch: 'readonly',
        process: 'readonly',
        setTimeout: 'readonly',
      },
    },
  },
  ...tseslint.configs.recommended.map((config) => ({ ...config, files: typescriptFiles })),
  {
    files: [
      'packages/{astronomy-core,assessment-core,tutoring-core,contracts,catalogue-schema}/src/**/*.{ts,tsx}',
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
                'react-dom',
                'react-dom/*',
                'three',
                'three/*',
                '@react-three/fiber',
                'express',
                'express/*',
                'mysql',
                'mysql2',
                'mysql2/*',
                'node:*',
                '@ufuq/web',
                '@ufuq/api',
                '@ufuq/catalogue',
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
    files: ['apps/web/src/**/*.{ts,tsx}'],
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': ['warn', { allowConstantExport: true }],
      'no-restricted-imports': [
        'error',
        {
          patterns: [
            {
              group: [
                '@ufuq/assessment-core',
                '@ufuq/assessment-core/*',
                '@ufuq/tutoring-core',
                '@ufuq/tutoring-core/*',
                '@ufuq/api',
                '@ufuq/api/*',
                '@ufuq/catalogue',
                '@ufuq/catalogue/*',
              ],
              message: 'The web application cannot import authoritative domains or tools.',
            },
          ],
        },
      ],
    },
  },
);
