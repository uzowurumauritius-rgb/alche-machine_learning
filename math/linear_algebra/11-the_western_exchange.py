#!/usr/bin/env python3
"""Module for transposing a numpy.ndarray."""


def np_transpose(matrix):
    """Returns the transpose of a numpy.ndarray as a new numpy.ndarray."""
    return matrix.transpose().copy()
