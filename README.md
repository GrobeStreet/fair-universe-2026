# FAIR Universe 2026 — Weak Lensing OoD Detection

**Independent, AI-assisted research. Not peer reviewed.**

This repository is the first externally scored implementation of **Bobby Research OS v1.0**. It targets the **NeurIPS 2026 FAIR Universe Weak Lensing ML Uncertainty Challenge — Phase 2**, an out-of-distribution (OoD) detection benchmark for weak-lensing cosmology.

> **Question -> Evidence -> Hypothesis -> Adversarial Tests -> Computation -> Falsification -> Replication -> External Score**

## Challenge objective

Given a weak-lensing convergence map `x`, produce a continuous anomaly score `t(x)` such that larger values indicate greater confidence that the map was generated outside the training distribution.

The organizers do **not** provide OoD examples or reveal the hidden OoD generative process. The project therefore focuses on robust detection of simulation/model mismatch rather than supervised classification of known anomalies.

## Official Phase 2 metric

The leaderboard score is the mean true-positive rate evaluated at **100 logarithmically spaced false-positive rates from 0.001 to 0.05**:

`score = mean_i TPR(FPR_i)`

This means performance in the extreme low-FPR tail matters much more than a generic full-range ROC-AUC.

## Dataset

The official training set contains weak-lensing convergence maps designed to mimic HSC Y3 observations:

- 101 spatially flat LCDM cosmologies spanning `(Omega_m, S8)`
- 256 realizations per cosmology
- map shape: `1424 x 176`
- 2 arcmin pixel resolution
- nuisance/systematic variation includes baryonic feedback and photometric-redshift uncertainty
- training samples are InD; Phase 2 test data contain an undisclosed subset generated under different physical assumptions

## Published baseline scores

The challenge white paper reports these Phase 2 public-test scores:

| Baseline | Score |
|---|---:|
| Power spectrum + chi-squared / p-value | **0.2143** |
| Autoencoder reconstruction error | **0.1307** |
| CNN summary + chi-squared / p-value | **0.1053** |
| Random score | **0.0128** |

Our first hard target is to reproduce an official baseline end-to-end. Only after that do we optimize.

## Research question

> Can a traceable, AI-assisted independent research pipeline develop an OoD detector for weak-lensing maps that robustly exceeds the strongest published FAIR Universe Phase 2 baseline under the official low-FPR metric and survives local adversarial validation?

See [`research_question.md`](research_question.md) and [`preregistration.md`](preregistration.md).

## Experimental program

The initial sequence is deliberately conservative:

1. **EXP-001 — Official power-spectrum baseline reproduction**
2. **EXP-002 — Frozen local validation and metric reproduction**
3. **EXP-003 — Power-spectrum residual / covariance variants**
4. **EXP-004 — Non-Gaussian hand-engineered statistics**
5. **EXP-005 — Learned representation-distance detector**
6. **EXP-006 — Synthetic-shift / self-supervised OoD training**
7. **EXP-007 — Low-FPR calibration and tail optimization**
8. **EXP-008 — Diversity-gated ensemble**

An experiment advances because it beats the frozen validation baseline, not because it sounds promising.

## Validation rules

- Keep the official baseline implementation reproducible and separate from experimental code.
- Freeze a local validation protocol before using leaderboard feedback for model selection.
- Treat Codabench submissions as scarce external measurements, not a hyperparameter oracle.
- Track every submission in `submissions/registry.csv`.
- Preserve failed experiments and negative results.
- Report performance at the official FPR grid and also inspect per-FPR behavior.
- No claim of improvement is accepted without seed/ablation checks appropriate to the method.

## Repository map

- `challenge/CHALLENGE_SPEC.md` — source-grounded task specification
- `research_question.md` — falsifiable research question and decision criteria
- `preregistration.md` — pre-specified working research record
- `assumptions.yaml` — explicit assumptions and sensitivity tests
- `evidence/` — source, claim, and contradiction registries
- `experiments/registry.csv` — experiment ledger
- `submissions/registry.csv` — external leaderboard measurements
- `src/metrics/phase2.py` — local implementation of the Phase 2 score
- `tests/` — integrity and metric tests
- `reports/` — executive, technical, limitations, and reproducibility outputs
- `RESEARCH_CONSTITUTION.md` — epistemic rules inherited from Bobby Research OS

## Upstream sources

Authoritative challenge material lives upstream at:

- FAIR Universe challenge site
- FAIR Universe `Cosmology_Challenge` GitHub repository
- challenge white paper, arXiv:2604.14451
- Phase 2 Codabench competition

The upstream repository is pinned for reproducibility in [`upstream/README.md`](upstream/README.md).

## Reproduction

For repository-level checks:

```bash
make test
make reproduce
```

The official starting-kit notebooks and competition data remain upstream and are not vendored here. The first operational milestone is to reproduce the official power-spectrum Phase 2 baseline and record the first valid Codabench score.

## Current status

**BASELINE** — repository specialized; official baseline execution and first scored submission are the next decisive actions.
