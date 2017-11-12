"""
fpi - Fixed Point Iteration methods comparison.
"""

if __name__ != '__main__':
    exit()

# import local modules
import jacobi
import seidel
import sor
import matreader

# Ax = b
A = matreader.read()
