import numpy as np
def simpsons1by3(x,y):
    h = x[1]-x[0]
    n = len(x)
    sum = y[0] + y[n-1]
    for i in range(1,n-1):
        if(i % 2 == 0):
            sum += y[i]*2
        else:
            sum+= y[i]*4
    return (sum*h)/3

x_data = np.array([0, 1/2, 1, 3/2, 2])
y_data = np.array([1, 0.6064, 0.3674, 0.2231, 0.1353])
result = simpsons1by3(x_data,y_data)
print(result)

