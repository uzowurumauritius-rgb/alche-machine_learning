#!/usr/bin/env python3
"""Module for adding two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Adds two 2D matrices element-wise and returns a new matrix."""
    if len(mat1) != len(mat2):
        return None
    if len(mat1) == 0:
        return []
    if len(mat1[0]) != len(mat2[0]):
        return None
    return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(mat1, mat2)]
