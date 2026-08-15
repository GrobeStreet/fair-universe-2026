# Pre-Specified Working Research Record

Use **pre-specified in the working research record** unless a formal preregistration exists.

## Hypothesis

A detector that combines physically meaningful weak-lensing summaries and/or learned representations with explicit low-FPR calibration can outperform the strongest published Phase 2 baseline while remaining robust to nuisance variation represented in the InD training distribution.

## Primary test

Compare candidate methods against a frozen local validation protocol and then against the official Codabench Phase 2 score.

The first experiment is not an improvement attempt: it is reproduction of the official power-spectrum baseline.

## Primary metric

Mean TPR over 100 log-spaced FPR targets from 0.001 to 0.05, matching the official Phase 2 metric.

## Datasets and versions

- Official FAIR Universe weak-lensing training data.
- Official Phase 2 test data used only through the Codabench evaluation interface unless challenge rules provide downloadable test inputs.
- Upstream code pinned to FAIR-Universe/Cosmology_Challenge commit `4cebdff5dda220994263379df13ce801cfddb8fe` as the Phase 2 launch-era reference implementation.
- Any local synthetic OoD datasets must be versioned and clearly labeled as researcher-generated validation data, not organizer data.

## Inclusion / exclusion rules

- All official training samples are treated as InD.
- No hidden/test labels may be inferred, scraped, leaked, or manually reconstructed.
- Any sample filtering, masking, standardization, or augmentation must be logged in the corresponding experiment record.
- No candidate is promoted solely because of leaderboard improvement without local evidence supporting the change.

## Parameters and priors

Method-specific parameters must be recorded in `experiments/registry.csv` and/or a per-experiment config file. Baseline reproduction should follow the organizer starting kit before deviations are introduced.

## Planned robustness tests

- multiple random seeds for stochastic methods;
- split sensitivity for local validation;
- nuisance/systematic stratification where labels are available in training data;
- feature-family ablations;
- score calibration stability;
- synthetic OoD family holdout: tune on some shift families, evaluate on an unseen synthetic family;
- ensemble diversity analysis before ensembling.

## Null / calibration tests

- InD-vs-InD split should produce near-random discrimination;
- score distribution should not spuriously separate cosmology or nuisance strata that are intentionally part of the training distribution unless justified;
- random scores should reproduce approximately the organizer's random-reference behavior under sufficiently large local test samples;
- metric implementation is unit-tested on analytically simple ranking cases.

## Stopping rule

Stop or substantially redesign a method family when:

1. it fails to beat the frozen local baseline across repeated seeds/splits;
2. an apparent gain disappears under ablation;
3. improvement is visible only after adaptive leaderboard probing;
4. computational cost becomes disproportionate to information gained.

Final competition selection will favor the highest externally scored method that also satisfies the local robustness record, not necessarily the method with the most complex architecture.

## Known alternative explanations

- synthetic-shift overfitting;
- nuisance leakage;
- cosmology interpolation artifacts;
- accidental preprocessing differences from the official baseline;
- tail-estimation noise at very low FPR;
- repeated-submission leaderboard overfitting.

## Post-hoc boundary

Anything added after inspection of a decisive local or Codabench result must be labeled **POST-HOC** with date, rationale, and experiment ID.

This record was specialized for FAIR Universe Phase 2 on 2026-08-15 before the first project-specific scored submission was recorded in this repository.
