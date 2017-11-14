import numpy as np
from math import log

def norm1(x):
    return np.linalg.norm(x, ord=None, axis=None, keepdims=False)

def norm2(x):
    return np.linalg.norm(x, ord=np.inf, axis=None, keepdims=False)

def count_iterations(A, b, eps=1e-5):
    D = np.diagflat(np.diag(A))  #     [D, U, U]
    LU = A - D                   # A = [L, D, U]
    Dinv = np.linalg.inv(D)      #     [L, L, D]

    G = np.dot(-Dinv, LU)        # G = -D^-1 * (L+U)
    g = np.dot(Dinv, b)          # g = -D^-1 * b

    q = norm2(G)
    gnorm = norm1(g)

    print('eps', eps, 'q', q, 'gnorm', gnorm)
    N = -1
    try:
        N = log(eps * (1 - q) / gnorm) / log(q) + 1
    except ValueError:
        print("Can't count expected iterations, please change the norm.")
    finally:
        return int(N)
