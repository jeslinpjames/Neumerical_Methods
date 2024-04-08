def gaussSeidel(A, b, x):
    n = len(A)
    for i in range(0,n):
        d =  b[i]
        for j in range(0,n):
            if(j != i):
                d -= A[i][j] * x[j]
        x[i] = d / A[i][i]
    return x

n = 3
a = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
b = [4, 7, 3]
x = [0, 0, 0]

for i in range(0, 15):
    x = gaussSeidel(a, b, x)
    print(x)