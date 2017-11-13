import numpy as np

def jacobi(A, b, eps=10e-10):
    try:
        n = len(A)
        x = np.zeros_like(b)

        converge = False
        while not converge:
            x_new = np.zeros_like(x)
            for i in range(n):
                s1 = np.dot(A[i][ :i], x[:i])
                s2 = np.dot(A[i][i + 1:], x[i + 1:])
                x_new[i] = (b[i] - s1 - s2) / A[i][i]

            #print(np.dot(A, x) - b)
            converge = np.linalg.norm(x_new-x) <= eps
            x = x_new
    except KeyboardInterrupt:
        print(x)
    finally:
        return x
