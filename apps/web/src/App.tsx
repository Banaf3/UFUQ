import type { HealthResponse } from '@ufuq/contracts';

const scaffoldHealth: HealthResponse = {
  status: 'ok',
  service: 'web',
  phase: 'scaffold',
};

export function App() {
  return (
    <main className="health-shell">
      <section className="health-card" aria-labelledby="health-title">
        <p className="eyebrow">UFUQ</p>
        <h1 id="health-title">Repository scaffold is healthy</h1>
        <dl>
          <div>
            <dt>Web</dt>
            <dd>{scaffoldHealth.status.toUpperCase()}</dd>
          </div>
          <div>
            <dt>Phase</dt>
            <dd>{scaffoldHealth.phase}</dd>
          </div>
        </dl>
        <p>
          No astronomy, cultural-route, assessment, BKT, account, or persistence behavior is loaded.
        </p>
      </section>
    </main>
  );
}
