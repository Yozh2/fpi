import numpy as np
import littlemath as lm

def seidel(A, b, eps=10e-5):
    try:
        n = len(A)
        x = np.zeros_like(b)
        disps = list()          # disperancies for every iteration

        iterations = 0
        converge = False
        while not converge:
            x_new = np.copy(x)
            for i in range(n):
                s1 = sum(A[i][j] * x_new[j] for j in range(i))
                s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = (b[i] - s1 - s2) / A[i][i]

            # Count disperance
            new_disp = lm.norm1(np.dot(A, x) - b)
            disps.append([new_disp])

            converge = new_disp <= eps
            x = x_new
            iterations += 1
    except KeyboardInterrupt:
        print('Exiting. Intermediate results:')
    finally:
        return x, iterations, np.array(disps)
