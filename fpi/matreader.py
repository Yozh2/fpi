"""
matreader - A simple .smtx matrix reader.
"""

import os
import logging
import numpy as np

def check_dir(path=None):
    # Check if the matrix.smtx file exists
    if not os.path.exists(path):
        logging.error('File not found: ', path)
        raise FileNotFoundError

def read(path=None):
    """
    Read the matrix from .smtx file.
    [path] - path to the matrix.smtx file.
    """

    check_dir(path)
    # Read primary data from the first string
    with open(path, 'r') as smtx:
        N, matrices = map(int, smtx.readline().split())

    # Read the (N+1)xN sized input matrix
    input_matrix = np.loadtxt(path, skiprows=1)

    # A is the NxN sized matrix
    A = input_matrix[:][:N].copy()
    # b is the Nx1 sized matrix
    b = input_matrix[:][N:].copy().T
    return A, b

def read_vector(path=None):
    """
    Read the vector from .smtx file.
    [path] - path to the vector.smtx file.
    """

    check_dir(path)
    # Read the (N+1)xN sized input matrix
    input_matrix = np.loadtxt(path)
    return input_matrix
