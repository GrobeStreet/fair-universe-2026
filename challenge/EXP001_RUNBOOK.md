# EXP-001 Runbook — Official Phase 2 Power-Spectrum Baseline

Purpose: complete the first external reproduction before any optimization work.

## Frozen upstream

- Organizer repository: `FAIR-Universe/Cosmology_Challenge`
- Pinned commit: `4cebdff5dda220994263379df13ce801cfddb8fe`
- Starting kit: `Phase_2_Startingkit_WL_PSAnalysis.ipynb`
- Codabench competition: Phase 2 competition `10902`

## What the organizer requires

The official Phase 2 starting-kit documentation says that a scored submission requires the public training data and test data from the Codabench **Data** tab. The small `input_data` directory in the organizer repository is only a downsampled dataset for exercising the starting kit locally.

A valid submission is a ZIP containing exactly the expected `result.json` payload with a top-level `ood_scores` list of **10,000** floating-point scores. Larger scores must indicate greater confidence that a test sample is OoD.

## Execution order

1. Clone/check out the organizer repository at the frozen commit above.
2. Record the exact Python/environment package state before running the baseline.
3. Smoke-run the power-spectrum Phase 2 starting kit on the organizer's downsampled `input_data` to catch environment/runtime failures.
4. Obtain the official public Phase 2 training and test data from Codabench. Do not substitute synthetic or downsampled data for the scored run.
5. Run the unmodified official power-spectrum starting-kit path end to end on official data.
6. Preserve the generated 10,000 OoD scores before any optimization.
7. Package them as `result.json` inside the submission ZIP.
8. Run the repository submission validator before upload.
9. Upload the baseline artifact to Codabench.
10. Record the returned score, date, exact code commit, environment, and notes in `submissions/registry.csv`.
11. Update `experiments/registry.csv` and `STATUS.md`; only then close EXP-001.

## External reference

The published organizer reference score for the power-spectrum baseline is **0.2143** on the Phase 2 public test dataset. Reproduction need not match bit-for-bit, but any material discrepancy must be investigated and documented rather than silently tuned away.

## Hard boundaries

- No optimization before the official baseline is reproduced and externally scored.
- No claim that synthetic shifts approximate the hidden OoD mechanism.
- No claim of successful reproduction until Codabench accepts and scores the artifact.
- Preserve failed runs and discrepancies.

## Current manual boundary

GitHub-side preparation can be completed without credentials. The remaining external steps require access to the Codabench Phase 2 Data tab for the official datasets and, later, the authenticated submission upload.
