import numpy as np
import littlemath as lm

def jacobi(A, b, eps=1e-5):
    try:
        n = len(A)
        x = np.zeros_like(b)
        disps = np.empty([100000,1])          # disperancies for every iteration

        iterations = 0
        converge = False
        while not converge:
            x_new = np.zeros_like(x)
            for i in range(n):
                s1 = np.dot(A[i][ :i], x[:i])
                s2 = np.dot(A[i][i + 1:], x[i + 1:])
                x_new[i] = (b[i] - s1 - s2) / A[i][i]

            # Count disperance
            new_disp = lm.norm1(np.dot(A, x) - b)
            disps[iterations] = [new_disp]

            converge = new_disp <= eps
            x = x_new
            iterations += 1
    except KeyboardInterrupt:
        print('Exiting. Intermediate results:')
    finally:
        disps = np.trim_zeros(disps, 'b')   # remove trailing zeros
        return x, iterations, disps
