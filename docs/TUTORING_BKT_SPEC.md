# Tutoring and Bayesian Knowledge Tracing specification

## Knowledge components

The following separate learner skill states are **CONFIRMED**. “Separate” describes
storage/update boundaries; it does not assert statistical independence or prove that a
task isolates one skill.

| ID | Knowledge component | Evidence example |
|---|---|---|
| KC-01 | Identify Banat Na'sh | Select the approved pattern/member relation |
| KC-02 | Recognise Dhat al-Kursi | Select the approved pattern/member relation |
| KC-03 | Locate Al-Jady/Polaris | Select the approved star using the intended celestial cues |
| KC-04 | Estimate True North | Submit a north direction within the approved task tolerance |
| KC-05 | Derive Qibla from True North | Submit the location-specific Qibla bearing within tolerance |

One scored task has one primary KC. A multi-step lesson is represented as several scored tasks so an outcome is not credited ambiguously to multiple KCs. EDU-002 must approve the task-to-KC mapping, prerequisite controls, incidental-cue risk, and alternate-form equivalence; a primary-KC label alone is not validity evidence.

The ordered lesson is supplied by a versioned `LessonRoute`, whose steps reference
generic `GuidanceRelationship` records between `SkyPattern`, star, and direction nodes.
A route may use reviewed helper patterns, Banat Na'sh, or Dhat al-Kursi before Al-Jady,
then continue to True North and Qibla. `bkt-core` and `adaptive-policy` consume the
route's prerequisite/KC/scaffold references; they do not hardcode a Banat Na'sh-first
sequence. Exact routes, helper patterns, relationships, and cue configurations remain
subject to their content and BKT review gates.

## Model and parameters

For each learner and KC, standard four-parameter BKT uses:

- `P(L0)`: initial mastery probability;
- `P(T)`: probability of learning between opportunities;
- `P(G)`: correct response while unmastered (guess);
- `P(S)`: incorrect response while mastered (slip).

The report's provisional values are `L0=.20`, `T=.10`, `G=.20`, `S=.10`, and display/adaptive threshold `.85`. They are **CONFIRMED as reproducible report examples**, not approved production calibration. BKT-002 and BKT-003 are **MANUAL DOMAIN DECISIONS**.

Store the parameter set and model version used for every transition. Production values must be immutable by version; changing them does not silently rewrite historical mastery.

## Equations and update order

Let prior mastery be `p`. For a correct observation:

```text
posteriorCorrect = p(1-S) / [p(1-S) + (1-p)G]
```

For an incorrect observation:

```text
posteriorIncorrect = pS / [pS + (1-p)(1-G)]
```

Then apply learning transition exactly once:

```text
nextMastery = posterior + (1-posterior)T
```

Persist and name all three values: `priorMastery`, `posteriorAfterObservation`, and `nextMasteryAfterTransition`. Do not label the posterior as the final state or apply transition before evidence.

## Numerical constraints

- All inputs and outputs are finite and in `[0,1]`.
- Require `1-S > G`; a correct answer must be more likely when mastered than unmastered.
- Denominators must be positive; reject a degenerate parameter set rather than divide by zero.
- Use double-precision arithmetic, retain full stored precision, and compare against an
  independently generated high-precision oracle using a justified absolute/relative
  implementation tolerance recorded under BKT-002/each ExecPlan; round only for
  display. No convenient global tolerance is assumed near degenerate boundaries.
- With no forgetting in the approved baseline, `nextMastery >= posterior`.
- For an interior prior and possible, informative evidence, a correct observation
  posterior is greater than the prior.
- For an interior prior and possible, informative evidence, an incorrect posterior is
  lower than the prior, but the stored post-transition state need not be. For the
  provisional parameters its lower fixed point is
  `((1-G)T)/(1-S-G) = 0.1142857...`; below this point an incorrect response can still
  finish higher after learning transition. Correcting the report's blanket invariant is
  DEV-008.

## Reproducible worked examples

These reproduce and extend the report model without quoting it.

### Report correct-response example

For prior `.60`, `T=.10`, `G=.20`, `S=.10`:

```text
posterior = .60*.90 / (.60*.90 + .40*.20)
          = .870967741935...
next      = .870967741935 + (1-.870967741935)*.10
          = .883870967742...  (~.8839)
```

Companion incorrect result from `.60`:

```text
posterior = .60*.10 / (.60*.10 + .40*.80) = .157894736842...
next      = .242105263158...
```

Starting from `L0=.20`, expected transitioned states are:

| Sequence | After 1 | After 2 | After 3 |
|---|---:|---:|---:|
| Correct, correct, correct | .576470588235 | .873684210526 | .971984435798 |
| Incorrect, incorrect, incorrect | .127272727273 | .116112531969 | .114539890399 |
| Correct, incorrect, correct | .576470588235 | .230860534125 | .617134416544 |

Two correct observations from `.20` exceed the provisional `.85` threshold. This demonstrates why assisted evidence and independent confirmation cannot be left implicit.

## Scaffolding states

The proposed state model is DEV-004:

| State | Semantic intent | Evidence label |
|---|---|---|
| `GUIDED` | Full approved orientation/pattern cues and explicit instructional support | Assisted |
| `FADING` | Reduced approved cues; no direct target reveal | Assisted/fading |
| `INDEPENDENT` | Task-required neutral scene only; no instructional cue | Independent |

The exact cues for each KC are BKT-004. Every scenario/attempt stores the authoritative
server-issued cue IDs/version used to classify evidence, not a client claim that cues were
hidden. Optional client render-success/failure telemetry is stored separately as
untrusted diagnostic data. A failure to render can invalidate an attempt, but client
telemetry can never upgrade assisted evidence to independent. Accessibility
accommodations are recorded separately and must not automatically be treated as hints.

The pure adaptive policy consumes mastery/evidence history, current state, and an immutable policy version. It returns a next state and reason code. It may fade after approved evidence and restore support after approved struggle rules. “High slip rate” is not an input observation—`S` is a fixed parameter; DEV-007 corrects that terminology.

| From | Candidate transition | Status |
|---|---|---|
| `GUIDED` | Stay guided or move to `FADING` after the approved evidence rule | MANUAL DOMAIN DECISION BKT-004 |
| `FADING` | Return to `GUIDED`, stay, or move to `INDEPENDENT` | MANUAL DOMAIN DECISION BKT-004 |
| `INDEPENDENT` | Stay independent or restore approved support after struggle | MANUAL DOMAIN DECISION BKT-004 |
| Any state | Never transition solely because a client asks for a state or because a fixed `S` parameter is “high” | CLARIFIED / DEV-007 |

No numeric cutoff or consecutive-attempt count is implied by this table. The approved policy must specify inclusive boundaries, history window, assistance eligibility, and reason code for every branch.

## Observation and policy decision contract

Every accepted submitted task persists exactly one typed model decision:

| Kind | Required persisted meaning |
|---|---|
| `OBSERVATION` | Binary evidence, parameter/model version, prior, posterior, transitioned next mastery, prior/next revision, and eligibility reason |
| `TRANSITION_ONLY` | No correctness likelihood update; approved learning opportunity applies transition once, with prior/posterior naming made explicit and a reason |
| `NO_MODEL_UPDATE` | Attempt and reason are stored; mastery/revision remain unchanged and no null field is misread as a calculation failure |

The transaction always stores the immutable attempt, model-decision outcome (including
an explicit no-op), and scaffold-decision outcome. NFR-03 therefore requires a matching
decision record, not a fabricated probability change for every accepted submission.
BKT-001 must define invalid, no-response, timeout, abandonment, feedback-revealed
retry, and duplicate behavior as well as assisted correctness.

## Assisted and independent evidence

The report baseline updates BKT on correct/incorrect attempts. DEV-006 proposes that guided/fading correctness not count identically as independent evidence. BKT-001 must select and approve one reproducible policy, for example:

1. guided practice records the attempt but does not apply an observation update;
2. guided practice applies transition only; or
3. guided/fading responses use separately justified and calibrated parameters.

No option is selected here. The database and contracts must carry `observationEligible` and assistance metadata so the decision is explicit. Mastery threshold status and `independentRecallConfirmed` are distinct fields/concepts. Independent confirmation count, spacing, and reset/expiry are BKT-003.

BKT-005 governs every session purpose. Evaluation-only `PRE_TEST`, `POST_TEST`, and
`RECALL` responses must not accidentally train, apply `P(T)`, change scaffolding, or
influence later outcome items. If any is approved to initialize/update the model, the
mapping, timing, version, and effect on comparison groups are frozen in the protocol.
The attempt/session purpose therefore distinguishes `PRE_TEST`, `LEARNING`,
`POST_TEST`, and `RECALL` independently from assistance state.

## Runtime boundary and transaction

`bkt-core` is a pure deterministic package. It knows nothing about React, Three.js, HTTP, SQL, hints, users, or storage. `adaptive-policy` is separately pure and can depend on BKT result types. The API supplies the locked prior, monotonic learner/KC `masteryRevision`, expected scenario revision, and approved immutable configuration, then persists the returned decision in the same transaction as the immutable assessment attempt. Replays return the original result and never call the model twice. A stale expected revision is rejected and reissued rather than applied after newer learning evidence.

All five current-version mastery rows and initial scaffolds are provisioned atomically
before assessed scenario issuance. BKT-002 decides how an existing learner moves to a
new model/policy version. Version changes never continue an old chain silently; use an
approved new chain/mapping and retain historical states/results for the permitted audit
period.

## Sensitivity and validation plan

1. Unit-test the three sequences above, edge probabilities, invalid sets, monotonic posterior properties, transition order, and numerical stability.
2. Sweep plausible approved grids for `L0/T/G/S`, retaining `1-S>G`, across representative correct/incorrect and assisted/independent sequences.
3. Report attempts to threshold, false-mastery risk under guessing, recovery after errors, threshold crossings caused by transition, and results by KC.
4. Compare candidate hinted-evidence policies before BKT-001 approval.
5. If participant data are sufficient and ethics permits, estimate/calibrate per the frozen analysis plan; otherwise retain transparently expert-set parameters and report sensitivity rather than overfit.
6. Freeze parameter/policy versions before formal evaluation and never tune on post-test results.
7. For every randomized/property run, retain RNG seed, generator/version, case count,
   parameter-domain definition, and minimized counterexample.
8. Report policy-fixture concordance, assistance exposure, attempts to first independent
   success, threshold crossings without independent confirmation, restoration/fade
   counts, and false-mastery indicators. These describe model/policy behavior; EDU-003
   determines any causal claim.

## Educational limitations

BKT assumes a binary observation, a well-defined KC, conditional independence given latent mastery, stationary parameters, and a simple learn/no-forget transition. It can be unidentifiable or poorly calibrated with small data, and threshold crossing is an operational policy—not proof of conceptual learning. Visual hints can change guess/slip behavior and violate stationarity. Therefore UFUQ evaluates no-hint pre/post/recall performance, time, angular accuracy, and assistance separately; it does not present BKT probability as a religious, navigational, or educational certification.

Learner-facing progress defaults to qualitative, approved wording and independent-
evidence status. Raw probabilities, rounding, uncertainty language, and policy reason
text require BKT-003/004 approval so a displayed threshold is never presented as proof
of learning.
