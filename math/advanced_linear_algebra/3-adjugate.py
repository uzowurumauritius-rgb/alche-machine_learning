#!/usr/bin/env python3
"""Module for calculating the adjugate matrix of a matrix."""


def _determinant(matrix):
    """Helper to calculate the determinant of a square matrix."""
    if matrix == [[]]:
        return 1
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(n):
        sub = [row[:c] + row[c + 1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * _determinant(sub)
    return det


def adjugate(matrix):
    """Calculates the adjugate matrix of a non-empty square matrix."""
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")
    if n == 1:
        return [[1]]
    cofactors = []
    for i in range(n):
        row_cof = []
        for j in range(n):
            sub = [
                row[:j] + row[j + 1:]
                for r_idx, row in enumerate(matrix)
                if r_idx != i
            ]
            row_cof.append(((-1) ** (i + j)) * _determinant(sub))
        cofactors.append(row_cof)
    return [[cofactors[r][c] for r in range(n)] for c in range(n)]
