import numpy as np

from src.metrics.phase2 import phase2_score


def test_perfect_ranking_scores_one():
    y = np.array([0] * 2000 + [1] * 200)
    scores = np.array([0.0] * 2000 + [1.0] * 200)
    assert np.isclose(phase2_score(y, scores), 1.0)


def test_inverted_ranking_scores_zero_in_low_fpr_region():
    y = np.array([0] * 2000 + [1] * 200)
    scores = np.array([1.0] * 2000 + [0.0] * 200)
    assert np.isclose(phase2_score(y, scores), 0.0)


def test_rejects_single_class():
    y = np.zeros(100, dtype=int)
    scores = np.arange(100, dtype=float)
    try:
        phase2_score(y, scores)
    except ValueError:
        return
    raise AssertionError("Expected ValueError")
