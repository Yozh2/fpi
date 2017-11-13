import numpy as np

def seidel(A, b, eps=10e-5):
    try:
        n = len(A)
        x = np.zeros_like(b)

        iterations = 0
        converge = False
        while not converge:
            x_new = np.copy(x)
            for i in range(n):
                s1 = sum(A[i][j] * x_new[j] for j in range(i))
                s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = (b[i] - s1 - s2) / A[i][i]

            converge = np.linalg.norm(x_new-x) <= eps
            x = x_new
            iterations += 1

    except KeyboardInterrupt:
        print('Exiting. Intermediate results:')
    finally:
        return x, iterations
