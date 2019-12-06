import numpy as np
import math
from math import sqrt
#float_percision = '{:.4f}'.format
#np.set_printoptions(formatter={'float_kind':float_percision})

def decomp_cholesky(A):

    n = len(A)
    L = np.zeros((n, n))

    for i in range(n):

        for j in range(i+1):

            L[i][j] = A[i][j]

            for k in range(j):

                L[i][j] -= L[i][k]*L[j][k]

            if(i == j):

                L[i][j] = sqrt(L[j][j])

            else:

                L[i][j] /= L[j][j]

    return L


def solve_lower(L, b):

    n = len(L)
    y = np.copy(b)

    y[0] = b[0] / L[0][0]

    for i in range(1, n):

        for j in range(i):

            y[i] -= L[i][j]*y[j]

        y[i] /= L[i][i]

    return y
         

def solve_upper(U, y):

    n = len(U)
    x = np.copy(y)

    for i in range(n-1, -1, -1):

        for j in range(i+1, n):

            x[i] -= U[j][i]*x[j]

        x[i] /= U[i][i]

    return x
    

def solve_cholesky(L,b):

    y = solve_lower(L,b)
    x = solve_upper(L,y)

    return x


if __name__ == '__main__':

	N = 1000
	print('N = ', N)

	#Filling N*N array to initialize it
	A1 = np.zeros((N,N), float)
	A2 = np.zeros((N,N), float)

	b1 = np.zeros(N, float)
	b2 = np.ones(N, float) 

	#Fill arrays with the correspondant values
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

	L = decomp_cholesky(A1)
	x = solve_cholesky(L, b1)

	print('A1 x = b1 \n Ten median x are:')

	ml = len(x) // 2 - 5
	mu = len(x) // 2 + 5

	print(x[ml : mu])

	L = decomp_cholesky(A2)
	x = solve_cholesky(L, b2)

	print('A2 x = b2 \n Ten median x are:')

	ml = len(x) // 2 - 5
	mu = len(x) // 2 + 5

	print(x[ml : mu])
