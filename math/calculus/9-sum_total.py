#!/usr/bin/env python3
"""Module to compute the sum of squares from 1 to n without loops."""


def summation_i_squared(n):
    """Calculates the sum of i squared from i = 1 to n.

    Args:
        n: Positive integer upper limit of summation.

    Returns:
        Integer value of the summation, or None if n is invalid.
    """
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        return None
    return (n * (n + 1) * (2 * n + 1)) // 6
