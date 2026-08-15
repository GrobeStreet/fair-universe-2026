"""FAIR Universe Phase 2 metric.

Computes mean TPR at 100 logarithmically spaced FPR targets in [0.001, 0.05].
Higher anomaly scores must indicate greater OoD confidence.
"""

from __future__ import annotations

import numpy as np


def _roc_points(y_true: np.ndarray, scores: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    y_true = np.asarray(y_true, dtype=int)
    scores = np.asarray(scores, dtype=float)

    if y_true.ndim != 1 or scores.ndim != 1 or len(y_true) != len(scores):
        raise ValueError("y_true and scores must be one-dimensional arrays of equal length")
    if not np.isin(y_true, [0, 1]).all():
        raise ValueError("y_true must contain only 0 (InD) and 1 (OoD)")
    if not np.isfinite(scores).all():
        raise ValueError("scores must be finite")

    pos = int(y_true.sum())
    neg = int(len(y_true) - pos)
    if pos == 0 or neg == 0:
        raise ValueError("metric requires at least one InD and one OoD sample")

    order = np.argsort(-scores, kind="mergesort")
    y = y_true[order]
    s = scores[order]

    tp = np.cumsum(y == 1)
    fp = np.cumsum(y == 0)

    distinct = np.r_[np.where(np.diff(s) != 0)[0], len(s) - 1]
    tpr = tp[distinct] / pos
    fpr = fp[distinct] / neg

    # Include origin for interpolation below the first achieved FPR.
    return np.r_[0.0, fpr], np.r_[0.0, tpr]


def phase2_score(
    y_true: np.ndarray,
    scores: np.ndarray,
    n_fpr: int = 100,
    fpr_min: float = 0.001,
    fpr_max: float = 0.05,
) -> float:
    """Return the FAIR Universe Phase 2 score.

    The ROC TPR is linearly interpolated at log-spaced FPR targets. This implementation
    is intended for local validation and should be checked against organizer scoring
    behavior before it is treated as authoritative.
    """

    if not (0.0 < fpr_min < fpr_max <= 1.0):
        raise ValueError("require 0 < fpr_min < fpr_max <= 1")
    if n_fpr < 1:
        raise ValueError("n_fpr must be positive")

    fpr, tpr = _roc_points(y_true, scores)
    targets = np.geomspace(fpr_min, fpr_max, n_fpr)
    interp_tpr = np.interp(targets, fpr, tpr)
    return float(np.mean(interp_tpr))
