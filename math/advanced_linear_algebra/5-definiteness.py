#!/usr/bin/env python3
"""Module for calculating the definiteness of a matrix."""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a symmetric numpy.ndarray."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")
    if (
        matrix.ndim != 2
        or matrix.shape[0] == 0
        or matrix.shape[0] != matrix.shape[1]
        or not np.issubdtype(matrix.dtype, np.number)
        or not np.all(np.isfinite(matrix))
    ):
        return None
    if not np.allclose(matrix, matrix.T):
        return None
    evals = np.linalg.eigvalsh(matrix)
    if np.all(evals > 1e-10):
        return "Positive definite"
    if np.all(evals >= -1e-10):
        return "Positive semi-definite"
    if np.all(evals < -1e-10):
        return "Negative definite"
    if np.all(evals <= 1e-10):
        return "Negative semi-definite"
    return "Indefinite"
