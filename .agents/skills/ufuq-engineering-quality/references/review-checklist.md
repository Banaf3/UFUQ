# Engineering quality review checklist

- [ ] The engineering claim and affected phase gate are explicit.
- [ ] Facts, project decisions, provisional choices, and unresolved questions are
  separated.
- [ ] A concrete quality attribute, dependency violation, observed failure, or
  significant maintenance cost justifies each major change.
- [ ] All affected workspaces, public exports, imports, TypeScript references, scripts,
  and CI paths were inspected.
- [ ] Pure domain packages remain framework, I/O, persistence, and browser independent.
- [ ] Runtime code cannot import tools or private workspace `src`/`dist` paths.
- [ ] Active test suites fail closed and no skipped/empty suite is reported as passed.
- [ ] Scientific claims use an independent reference and record provenance.
- [ ] Commands, environment assumptions, exit codes, and failures are reproducible.
- [ ] The recommendation is proportionate to a one-developer FYP.
- [ ] Risks of changing and keeping the structure are both stated.
- [ ] No approved decision or report requirement changed silently.

