def trapezodial(x,y):
    h = x[1]-x[0]
    n = len(x)
    sum = y[0] + y[n-1]
    for i in range(1,n-1):
       sum += y[i] * 2
    return (sum*h)/2

x_data = [0, 1/2, 1, 3/2, 2]
y_data = [1, 0.6064, 0.3674, 0.2231, 0.1353]
result = trapezodial(x_data,y_data)
print(result)

