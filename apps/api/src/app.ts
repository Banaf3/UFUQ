import express from 'express';

import type { HealthResponse } from '@ufuq/contracts';

export function createApp(): express.Express {
  const app = express();
  app.disable('x-powered-by');

  app.get('/health', (_request, response) => {
    const body: HealthResponse = {
      status: 'ok',
      service: 'api',
      phase: 'scaffold',
    };
    response.status(200).json(body);
  });

  return app;
}
