#!/usr/bin/env python3
"""Module to compute the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Calculates the indefinite integral of a polynomial.

    Args:
        poly: List of int/float coefficients where index i is power x^i.
        C: Integer integration constant (defaults to 0).

    Returns:
        New minimal list of integral coefficients, or None if invalid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if isinstance(C, bool) or not isinstance(C, int):
        return None
    for coeff in poly:
        if isinstance(coeff, bool) or not isinstance(coeff, (int, float)):
            return None

    integral = [C]
    for power, coeff in enumerate(poly):
        deg = power + 1
        if isinstance(coeff, int) and coeff % deg == 0:
            val = coeff // deg
        else:
            val = coeff / deg
            if isinstance(val, float) and val.is_integer():
                val = int(val)
        integral.append(val)

    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral
