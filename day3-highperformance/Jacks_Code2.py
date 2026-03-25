#%%
import numpy as np

# a. Create a null vector of size 10 but the fifth value which is 1
a = np.zeros(10)
a[4] = 1  # index 4 = fifth element
print("a:", a)

# b. Create a vector with values ranging from 10 to 49
b = np.arange(10, 50)
print("b:", b)

# c. Reverse a vector (first element becomes last)
c = b[::-1]
print("c (reversed b):", c)

# d. Create a 3x3 matrix with values ranging from 0 to 8
d = np.arange(9).reshape(3, 3)
print("d:\n", d)

# e. Find indices of non-zero elements from [1,2,0,0,4,0]
e_array = np.array([1, 2, 0, 0, 4, 0])
e = np.nonzero(e_array)
print("e (non-zero indices):", e)

# f. Create a random vector of size 30 and find the mean value
f = np.random.random(30)
f_mean = f.mean()
print("f (random vector):", f)
print("f mean:", f_mean)

# g. Create a 2D array with 1 on the border and 0 inside
g = np.ones((5, 5))
g[1:-1, 1:-1] = 0
print("g:\n", g)

# h. Create an 8x8 matrix and fill it with a checkerboard pattern
h = np.zeros((8, 8), dtype=int)
h[::2, ::2] = 1
h[1::2, 1::2] = 1
print("h:\n", h)

# i. Create a checkerboard 8x8 matrix using the tile function
tile_pattern = np.array([[1, 0], [0, 1]])
i = np.tile(tile_pattern, (4, 4))
print("i:\n", i)

# j. Given a 1D array, negate all elements which are between 3 and 8, in place
j = np.array([1, 5, 7, 2, 9, 4, 8])
j[(j > 3) & (j < 8)] *= -1
print("j:", j)