#%%
import numpy as np
from scipy import linalg
from timeit import timeit as tit


A = np.array([np.array([1,-2, 3]),
            np.array([4, 5, 6]),
            np.array([7, 1, 9])])

b = np.array([1, 2, 3])

def solve():
    x = linalg.solve(A, b)
    print(x)
    return x

print(tit(solve, number=1), '\n')


# Solve the eigenvalue problem
def eig():
    values, vectors = linalg.eig(A)
    # Print results
    print("Eigenvalues:")
    print(values.real)
    print("Eigenvectors:")
    print(vectors)
    return values, vectors

print(tit(eig, number=1))
