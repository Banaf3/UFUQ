import { createApp } from './app.js';

const port = Number.parseInt(process.env.PORT ?? '4174', 10);
const app = createApp();

app.listen(port, '127.0.0.1', () => {
  console.log(`UFUQ scaffold API listening on http://127.0.0.1:${port}`);
});
