import numpy as np
def gaussElimination(A,b):
    n = len(A)
    M = A.tolist()
    
    for i in range(n):
        M[i].append(b[i])
    
    for k in range(n):
        for i in range(k,n):
            if abs(M[k][k])<abs(M[i][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        for j in  range(k+1,n):
            q = M[j][k] / M[k][k]
            for m in range(k,n+1):
                M[j][m] -= q * M[k][m]
        
        x = [0 for _ in range(n)]
        x[n-1] = M[n-1][n] / M[n-1][n-1]
        for i in range(n-1,-1,-1):
            z = 0
            for j in range(i+1, n):
                z += M[i][j] * x[j]
                x[i] = (M[i][n] - z) / M[i][i]

    return x


A = np.array([[2,  2, 1], [4,  2,  3], [1,  1,  1]], dtype=float)
b = np.array([6,  4,  0], dtype=float)

x = gaussElimination(A, b)
print(f'Solution: {x}')


