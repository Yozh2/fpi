import numpy as np
import littlemath as lm

def seidel(A, b, eps=1e-5):
    try:
        n = len(A)
        x = np.zeros_like(b)
        residuals = np.empty([1000000,1])          # residuals for every iteration

        iterations = 0
        converge = False
        while not converge:
            x_new = np.copy(x)
            for i in range(n):
                s1 = sum(A[i][j] * x_new[j] for j in range(i))
                s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = (b[i] - s1 - s2) / A[i][i]

            # Count residual
            new_res = lm.norm1(np.dot(A, x) - b)
            residuals[iterations] = [new_res]
            print('seidel', iterations, 'iteration residual:', new_res)

            converge = new_res <= eps
            x = x_new
            iterations += 1
    except KeyboardInterrupt:
        print('Exiting. Intermediate results:')
    finally:
        residuals = np.trim_zeros(residuals, 'b')   # remove trailing zeros
        return x, iterations, residuals
