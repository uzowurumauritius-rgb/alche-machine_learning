#!/usr/bin/env python3
"""Module for 2D matrix multiplication."""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication of two 2D matrices."""
    if not mat1 or not mat2 or len(mat1[0]) != len(mat2):
        return None
    return [
        [sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)]
        for row in mat1
    ]
