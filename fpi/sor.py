import numpy as np

def sor(A, b, eps=10e-7):
    try:
        n = len(A)
        b = np.dot(A.T, b)
        A = np.dot(A.T, A)
        x = np.zeros_like(b)

        # Optimal parameter count
        eig = np.linalg.eig(A)[0]
        max_eig = max(eig)
        min_eig = min(eig)
        w = 2 / (max_eig  + min_eig)

        iterations = 0
        converge = False
        while not converge:
            x_new = np.copy(x)
            for i in range(n):
                s1 = sum(A[i][j] * x_new[j] for j in range(i))
                s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = (b[i] - s1 - s2) / A[i][i]       # Like in seidel
                x_new[i] = w * x_new[i] + (1-w)*x[i]        # Shift to SOR

            converge = np.linalg.norm(x_new-x) <= eps
            x = x_new
            iterations += 1

    except KeyboardInterrupt:
        print('Exiting. Intermediate results:')
    finally:
        return x, iterations
