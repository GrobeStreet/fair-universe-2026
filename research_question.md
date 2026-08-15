# Research Question

## Primary question

Can a traceable, AI-assisted independent research pipeline develop an out-of-distribution detector for weak-lensing convergence maps that robustly exceeds the strongest published FAIR Universe Phase 2 baseline under the official low-FPR metric and survives local adversarial validation?

## Primary outcome

Official Phase 2 score: mean true-positive rate over 100 logarithmically spaced false-positive rates from 0.001 to 0.05.

Secondary diagnostics:

- TPR at each official FPR point
- ROC-AUC for context only
- seed-to-seed variability where applicable
- calibration/tail stability on local validation splits

## Success criterion

Primary success: a valid Codabench submission whose official score exceeds the strongest published Phase 2 baseline of 0.2143, with the improvement supported by a frozen local validation protocol and method-appropriate robustness checks.

Stretch success: a reproducible method that remains competitive under multiple local synthetic-shift families and whose gains are not attributable to one seed, one arbitrary split, or leaderboard overfitting.

## Failure criterion

The central hypothesis is materially weakened if:

- the official baseline cannot be reproduced within a reasonable implementation tolerance;
- apparent improvements vanish under frozen local validation or seed/ablation checks;
- gains depend on repeated leaderboard probing rather than locally justified changes;
- the detector is brittle to plausible nuisance/systematic variation already represented in the InD training distribution;
- the final method does not exceed the published 0.2143 reference score.

## Competing explanations

- H1: Added statistics or learned representations capture hidden physical/model mismatch not visible to the baseline.
- H2: Apparent gains come from overfitting the local synthetic OoD generator rather than true generalization.
- H3: Apparent gains come from leaderboard feedback leakage / adaptive submission choices.
- H4: Improvements reflect better tail calibration rather than genuinely better ranking of OoD samples.
- H5: The official power-spectrum baseline is already close to the information ceiling available without access to hidden OoD structure.

## Highest-value next experiment

**EXP-001: reproduce the official power-spectrum Phase 2 baseline end-to-end and record the first valid external score.**
