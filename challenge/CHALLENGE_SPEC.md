# FAIR Universe Phase 2 — Challenge Specification

This file records the challenge facts that govern this repository. It is based on the official FAIR Universe challenge materials and white paper (arXiv:2604.14451).

## Task

For each weak-lensing convergence map `x`, construct a continuous score `t(x)` such that larger values indicate greater confidence that `x` is out-of-distribution (OoD) relative to the training simulations.

The test set contains an undisclosed subset generated under different physical assumptions. Participants are not provided OoD examples or the hidden OoD generative process.

## Official metric

The Phase 2 score is

`score = (1/N) * sum_i TPR(FPR_i)`

with `N = 100` and `FPR_i` logarithmically spaced between `0.001` and `0.05`.

The metric emphasizes detection power at low false-positive rates. Full ROC-AUC is therefore secondary and must not be substituted for the official metric.

## Current organizer execution state

- Current organizer execution pin used by this repository: `f5def09c024071f50e1cfe537b39245550e3666d` (2026-08-17).
- The original launch pin `4cebdff5dda220994263379df13ce801cfddb8fe` is retained only as historical provenance.
- The organizer changed the Phase 2 notebooks, data/evaluation pages, and scoring code after launch.

## Training data facts

- 101 spatially flat LCDM cosmologies.
- Cosmological labels vary in `Omega_m` and `S8`.
- 256 noiseless weak-lensing maps per cosmology with varying realizations and nuisance parameters.
- Each map is `1424 x 176` pixels at 2 arcmin resolution.
- The maps represent the second redshift bin of the HSC Y3 WIDE12H subfield.
- Baryonic feedback and photometric-redshift uncertainty are sampled as nuisance/systematic effects in the training data.
- Each sample has a 5D label `(Omega_m, S8, T_AGN, f0, Delta_z)`.
- The current organizer download contains training plus public test data and is approximately 8.7 GB.

## Current public-test data

The current valid public test file is:

`WIDE12H_bin2_2arcmin_kappa_test_phase2_new_v2.npy`

The organizers replaced the earlier `*_test_phase2_new.npy` dataset on 2026-08-12 after identifying a numerical problem. Submissions based on the earlier test dataset were invalidated and the public leaderboard was reset.

## Critical eligibility rule: sample-independent inference

Every submitted method must evaluate each test sample independently.

The output for one test sample must not depend on the presence, absence, order, or values of any other test sample. The public test set must not be used collectively to fit, train, adapt, cluster, calibrate, normalize, rank, select, estimate densities, construct nearest-neighbor references, compute thresholds, pseudo-label, or otherwise modify the method.

This rules out transductive or test-set aggregation strategies for final ranking/prize eligibility. Any local experimentation in this repository must preserve this boundary.

## Official Phase 2 baselines

Reported on the public test dataset in the white paper:

| Method | Score |
|---|---:|
| Power spectrum + MCMC-derived chi-squared / p-value | 0.2143 |
| Autoencoder reconstruction error | 0.1307 |
| CNN + MCMC-derived chi-squared / p-value | 0.1053 |
| Random OoD scores | 0.0128 |

The organizers note that simple neural-network baselines underperform the power-spectrum method on some hidden OoD categories.

## Baseline logic

### Power-spectrum / CNN summary route

1. Produce a summary statistic `d`.
2. Infer best-fit cosmological parameters.
3. Evaluate a chi-squared goodness-of-fit statistic relative to the learned InD mean/covariance at the best-fit parameters.
4. Compare test chi-squared values with the InD training distribution.
5. Use negative p-value as the OoD score.

### Autoencoder route

1. Train an autoencoder only on InD training samples.
2. Compute reconstruction errors.
3. Compare test reconstruction-error behavior to the training reference distribution.
4. Convert that extremeness to an OoD score.

## Competition / registration constraints

Phase 2 submissions are open until **October 11, 2026, 23:59 UTC** according to the official challenge repository.

The organizer asks participants to register using an affiliation/institution/company email. Public-domain email registrations may not be approved automatically.

Final rankings are based on a private holdout rerun of packaged methods, so public-test performance is not sufficient by itself.

## Sources

- FAIR Universe official challenge website
- `FAIR-Universe/Cosmology_Challenge` official repository at current execution pin
- Dai et al., *FAIR Universe Weak Lensing ML Uncertainty Challenge: Handling Uncertainties and Distribution Shifts for Precision Cosmology*, arXiv:2604.14451
- Phase 2 Codabench competition

## Research interpretation

The hidden test process is intentionally unknown. This repository therefore treats local synthetic shifts as stress tests, not as approximations known to match the organizers' test distribution.
