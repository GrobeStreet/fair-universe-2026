# Project Status

**Status:** BASELINE

## Current bottleneck

The repository is specialized, but the official Phase 2 power-spectrum starting kit has not yet been executed end-to-end in this project and no project-specific Codabench score has been recorded.

## Next decisive action

Run **EXP-001**: reproduce the official power-spectrum Phase 2 baseline, create a valid submission, and record the external score in `submissions/registry.csv`.

No optimization work should supersede this reproduction milestone.

## EXP-001 execution gate

The experiment is complete only when all of the following are true:

- official Phase 2 power-spectrum baseline runs on official data;
- exact environment and pinned upstream commit are recorded;
- local metric behavior is validated;
- a valid Phase 2 submission artifact is produced;
- the artifact is accepted and scored by Codabench;
- score/date/code commit are written to `submissions/registry.csv`;
- `experiments/registry.csv` is updated with the observed result.

Until then, claims remain at **baseline/reproduction-in-progress** status.

## Owner

Robert "Bobby" Morong (`GrobeStreet`)

## External benchmark

NeurIPS 2026 FAIR Universe Weak Lensing ML Uncertainty Challenge — Phase 2.

## Deadline

October 11, 2026, 23:59 UTC.

## Last updated

2026-08-20
