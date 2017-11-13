import numpy as np

def sor(A, b, eps=10e-7,w=1.5):
    b = np.dot(A.T,b)
    A = np.dot(A.T, A)
    n = len(A)
    x = np.zeros_like(b)
    iterations = 0
    converge = False
    while not converge:
        x_new = np.copy(x)
        iterations += 1
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
            x_new[i] = w * x_new[i] + (1-w)*x[i]
        print(x_new)
        converge = np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new
    
    return x




