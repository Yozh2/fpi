import numpy as np

def jacobi(A, b, eps=10e-10):
    n = len(A)
    x = np.zeros_like(b)

    converge = False
    while not converge:
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i][ :i], x[:i])
            s2 = np.dot(A[i][i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new

    return x
