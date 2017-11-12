"""
matreader - A simple .smtx matrix reader.
"""

import os
import logging
import numpy as np

def read(path=None):
    """
    Read the matrix from .smtx file.
    [path] - path to the matrix.smtx file.
    """

    # Check if the matrix.smtx file exists
    if not os.path.exists(path):
        logging.error('File not found: ', path)
        raise FileNotFoundError

    # Read primary data from the first string
    with open(path, 'r') as smtx:
        N, matrices = map(int, smtx.readline().split())

    # Read the (N+1)xN sized input matrix
    input_matrix = np.loadtxt(path, skiprows=1)

    # A is the NxN sized matrix
    A = input_matrix[:][:N].copy()
    # Transposed b is the 1xN sized matrix
    b = input_matrix[:][N:].copy()
    return A, b
