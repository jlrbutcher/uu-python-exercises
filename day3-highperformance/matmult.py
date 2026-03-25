#%%
# Program to multiply two matrices using nested loops
import random
import timeit

def func1(N=10):

    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])

    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])

    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))

    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result

t1 = timeit.timeit(func1, number=10)

import numpy as np

def func2(N=10):
    #####################################

    # Create random matrices using NumPy
    X = np.random.randint(0, 101, size=(N, N))
    Y = np.random.randint(0, 101, size=(N, N+1))

    # Perform matrix multiplication efficiently
    result = X @ Y  # equivalent to np.dot(X, Y)

    return result

t2 = timeit.timeit(func2, number=10)

print(t1)
print(t2)