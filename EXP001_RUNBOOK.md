# EXP-001 Runbook — FAIR Universe Phase 2 Power-Spectrum Baseline

Goal: reproduce the official Phase 2 power-spectrum baseline end-to-end and obtain the first project-specific Codabench score before any optimization work.

## Frozen upstream

- Organizer repository: `FAIR-Universe/Cosmology_Challenge`
- Pinned commit: `4cebdff5dda220994263379df13ce801cfddb8fe`
- Starting kit: `Phase_2_Startingkit_WL_PSAnalysis.ipynb`
- Published public baseline score: `0.2143`

## Official submission contract

The Phase 2 sample submission is a ZIP containing exactly one JSON file named `result.json` with:

```json
{
  "ood_scores": [0.0, 0.0]
}
```

For a full competition submission, `ood_scores` must contain 10,000 floating-point scores in test-sample order. Larger values must indicate greater confidence that the sample is out-of-distribution.

The official score is the mean TPR evaluated at 100 logarithmically spaced FPR values from 0.001 through 0.05.

## Execution order

1. Use the organizer's pinned power-spectrum Phase 2 notebook without optimization.
2. Record the Python environment and dependency versions actually used.
3. First run against the repository's downsampled `input_data` to confirm the notebook executes locally / in Colab.
4. Download the official public Phase 2 training and test data from the competition Data tab.
5. Run the baseline on the official public data.
6. Confirm that the produced score vector:
   - has length 10,000;
   - contains finite numeric values;
   - preserves test-set order;
   - uses larger score = more OoD confidence.
7. Write `result.json`, ZIP it as the competition submission artifact, and inspect the archive before upload.
8. Submit to Phase 2 Codabench.
9. Record:
   - Codabench score;
   - submission date/time;
   - repository commit;
   - upstream commit;
   - environment;
   - any deviations/errors.
10. Update `submissions/registry.csv`, `experiments/registry.csv`, and `STATUS.md`.
11. Only after EXP-001 is complete may optimization work begin.

## Current hard blocker

The full public Phase 2 training and test datasets are distributed through the competition Data tab. Access/download may require the participant's logged-in Codabench session. The GitHub repository only includes downsampled example data suitable for smoke-testing the starting kit, not the full scoring run.

## Zero-cost gate

Do not purchase compute, API credits, storage, or software for EXP-001. Use the organizer-provided data, local hardware, or free execution resources only. If a step requires payment, stop and reassess.

## Evidence standard

Do not mark EXP-001 complete until an external Codabench score is recorded. A locally generated submission file alone is not sufficient.
