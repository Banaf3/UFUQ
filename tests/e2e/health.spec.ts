import { expect, test } from '@playwright/test';

test('web and API scaffold health surfaces respond', async ({ page, request }) => {
  await page.goto('/');

  await expect(page.getByRole('heading', { name: 'Repository scaffold is healthy' })).toBeVisible();
  await expect(page.getByText('No astronomy, cultural-route, assessment, BKT')).toBeVisible();

  const apiResponse = await request.get('http://127.0.0.1:4174/health');
  expect(apiResponse.ok()).toBe(true);
  await expect(apiResponse.json()).resolves.toEqual({
    status: 'ok',
    service: 'api',
    phase: 'scaffold',
  });
});
