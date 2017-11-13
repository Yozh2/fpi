import numpy as np

def norm1(x):
    return max(x)

def jacobi(A, b, eps=10e-5):
    try:
        n = len(A)
        x = np.zeros_like(b)
        disps = list()          # disperancies for every iteration

        converge = False
        while not converge:
            x_new = np.zeros_like(x)
            for i in range(n):
                s1 = np.dot(A[i][ :i], x[:i])
                s2 = np.dot(A[i][i + 1:], x[i + 1:])
                x_new[i] = (b[i] - s1 - s2) / A[i][i]

            cur_disp =
            converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
            x = x_new
            iterations += 1
    except KeyboardInterrupt:
        print('Exiting. Intermediate results:')
    finally:
        return x, iterations
