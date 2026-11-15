#!/usr/bin/env python3
"""Module for element-wise operations on numpy.ndarrays."""


def np_elementwise(mat1, mat2):
    """Performs element-wise add, sub, mul, and div."""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
