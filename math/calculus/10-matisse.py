#!/usr/bin/env python3
"""Module to compute the derivative of a polynomial."""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial represented by coefficients.

    Args:
        poly: List of int/float coefficients where index i is power x^i.

    Returns:
        New list of derivative coefficients, [0] if derivative is 0, or None
        if poly is invalid.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    for coeff in poly:
        if isinstance(coeff, bool) or not isinstance(coeff, (int, float)):
            return None
    if len(poly) == 1:
        return [0]
    deriv = [poly[i] * i for i in range(1, len(poly))]
    while len(deriv) > 1 and deriv[-1] == 0:
        deriv.pop()
    if all(v == 0 for v in deriv):
        return [0]
    return deriv
