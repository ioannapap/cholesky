import numpy as np
import scipy as sp
from scipy.linalg import cho_factor, cho_solve

N = 1000

#Filling N*N array to initialize it

A1 = np.zeros((N,N), int)
A2 = np.zeros((N,N), int)

b1 = np.zeros((N,1), int)
b2 = np.ones((N,1), int) 

#Filling arrays with the correspondant values

np.fill_diagonal(A1, 6)
np.fill_diagonal(A1[1:], -4)
np.fill_diagonal(A1[:, 1:], -4)
np.fill_diagonal(A1[2:], 1)
np.fill_diagonal(A1[:, 2:], 1)

np.fill_diagonal(A2, 7)
np.fill_diagonal(A2[1:], -4)
np.fill_diagonal(A2[:, 1:], -4)
np.fill_diagonal(A2[2:], 1)
np.fill_diagonal(A2[:, 2:], 1)

b1[0] = 3
b1[1] = -1
b1[-2] = -1
b1[-1] = 3

b2[0] = 4
b2[1] = 0
b2[-2] = 0
b2[-1] = 4

print(A1)
print(A2)

print(b1)
print(b2)

A, low = cho_factor(A1)
x = cho_solve((A, low), b1)
print('A1 x = b1 solution for x is:')
print(x)

A, low = cho_factor(A2)
x = cho_solve((A, low), b2)
print('A2 x = b2 solution for x is:')
print(x)

