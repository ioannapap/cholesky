import numpy as np
import scipy as sp
from scipy.linalg import cho_factor, cho_solve
import time
start_time = time.time()
#float_formatter = '{:.4f}'.format
#np.set_printoptions(formatter={'float_kind':float_formatter})

N = 10000
print('N: ', N)

#Filling N*N array to initialize it

A1 = np.zeros((N,N), float)
A2 = np.zeros((N,N), float)

b1 = np.zeros((N,1), float)
b2 = np.ones((N,1), float) 

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

#print(A1)
#print(A2)
#print(b1)
#print(b2)

A, low = cho_factor(A1)
x = cho_solve((A, low), b1)

print('A1 x = b1 \n Ten median x are:')

ml = len(x) // 2 - 5
mu = len(x) // 2 + 5

print(x[ml : mu])

A, low = cho_factor(A2)
x = cho_solve((A, low), b2)

print('A2 x = b2 \n Ten median x are:')

ml = len(x) // 2 - 5
mu = len(x) // 2 + 5

print(x[ml : mu])

print("--- %s seconds ---" % (time.time() - start_time))