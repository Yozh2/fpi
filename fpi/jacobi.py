import numpy as np
import littlemath as lm

def jacobi(A, b, eps=1e-5):
    try:
        print(lm.count_iterations(A, b, eps), 'iterations expected')

        n = len(A)
        x = np.zeros_like(b)
        residuals = np.empty([100000,1])          # residuals for every iteration

        iterations = 0
        converge = False
        while not converge:
            x_new = np.zeros_like(x)
            for i in range(n):
                s1 = np.dot(A[i][ :i], x[:i])
                s2 = np.dot(A[i][i + 1:], x[i + 1:])
                x_new[i] = (b[i] - s1 - s2) / A[i][i]

            # Count residual
            new_res = lm.norm1(np.dot(A, x) - b)
            residuals[iterations] = [new_res]

            converge = new_res <= eps
            x = x_new
            iterations += 1
    except KeyboardInterrupt:
        print('Exiting. Intermediate results:')
    finally:
        residuals = np.trim_zeros(residuals, 'b')   # remove trailing zeros
        return x, iterations, residuals
