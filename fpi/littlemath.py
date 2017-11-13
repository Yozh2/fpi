import numpy as np

def norm1(x):
    return np.linalg.norm(x, ord=None, axis=None, keepdims=False)

def norm2(x):
    return np.linalg.norm(x, ord=inf, exis=None, keepdims=False)
