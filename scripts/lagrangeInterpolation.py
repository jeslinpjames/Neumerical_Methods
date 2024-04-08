import numpy as np

def lagrange_interpolation(x,y, val):
    n = len(x)
    L = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i!=j:
                p *= ((val-x[j])/(x[i]-x[j]))
        L+= p * y[i]
    return L

x_data = np.array([0, 2, 3, 5, 6])
y_data = np.array([5, 7, 8, 10, 12])
x_interp = 4 

print("Interpolated value at x =", x_interp, "is", lagrange_interpolation(x_data, y_data, x_interp))

