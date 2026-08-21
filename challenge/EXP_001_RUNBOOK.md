# EXP-001 Runbook — Official Phase 2 Power-Spectrum Baseline

Purpose: reproduce the organizer's Phase 2 power-spectrum baseline before any optimization work.

## Frozen upstream references

- Organizer repository: `FAIR-Universe/Cosmology_Challenge`
- Organizer branch: `master`
- Repository pin used by this project: `4cebdff5dda220994263379df13ce801cfddb8fe`
- Official notebook: `Phase_2_Startingkit_WL_PSAnalysis.ipynb`
- Official competition: Codabench Phase 2 competition 10902
- Published power-spectrum baseline score: `0.2143`

## Submission contract

The official Phase 2 starting-kit documentation states that a valid submission is a ZIP containing exactly one JSON file named `result.json` with a top-level `ood_scores` list containing 10,000 floating-point OoD scores. Scores must increase monotonically with confidence that a sample is OoD.

Expected structure:

```text
submission.zip
└── result.json
```

Expected JSON shape:

```json
{
  "ood_scores": [0.0, 0.0]
}
```

The real list must contain exactly 10,000 items.

## Official metric

For each test sample, produce a continuous OoD score `t(x)` where larger values mean more confidence that the sample is OoD.

The leaderboard score is the mean TPR evaluated at 100 logarithmically spaced FPR values from 0.001 through 0.05.

Do not substitute full ROC-AUC for the official metric.

## Baseline logic to reproduce

For the power-spectrum route, the organizer starting kit:

1. computes a power-spectrum summary statistic `d`;
2. estimates best-fit cosmological parameters;
3. evaluates a chi-squared goodness-of-fit statistic relative to the InD mean/covariance at the best-fit parameters;
4. compares test chi-squared values against the InD training distribution;
5. uses negative p-value as the OoD score.

## Execution order

### Gate A — lightweight organizer-code smoke test

Clone the official repository and run the organizer notebook against the repository's included downsampled data. This verifies environment compatibility and the baseline path without downloading the full competition dataset.

Record:

- OS / Python version
- exact organizer commit
- package environment
- whether all notebook cells execute
- any warnings/errors

### Gate B — full official-data reproduction

Download the public training data and public test data from the Codabench Data tab. The organizer explicitly requires those full datasets to train the baseline and generate a scoreable submission.

Run the same power-spectrum pipeline on the full public data without optimization or architecture changes.

### Gate C — local submission validation

Before upload, verify:

- archive contains `result.json` at the ZIP root;
- JSON has exactly one required `ood_scores` field;
- `ood_scores` is a list of exactly 10,000 finite numeric values;
- no NaN/Inf values;
- ordering matches the official public test data order;
- scores are oriented so larger values mean greater OoD confidence.

### Gate D — external score

Submit the frozen artifact to Codabench.

Record in `submissions/registry.csv`:

- date/time UTC
- repository commit
- organizer commit
- method name
- artifact checksum
- Codabench score
- notes

Then update `experiments/registry.csv`, `STATUS.md`, and GitHub issue #1.

## Stop rule

EXP-001 is not complete until a valid Codabench score is recorded. No optimization work should supersede this reproduction milestone.

If the reproduced score materially differs from the organizer's published `0.2143`, preserve the discrepancy and investigate it rather than tuning until it disappears.
