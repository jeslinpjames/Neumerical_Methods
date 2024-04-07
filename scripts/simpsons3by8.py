def simpsons3by8(x,y):
    h = x[1]-x[0]
    n = len(x)
    sum = y[0] + y[n-1]
    for i in range(1,n-1):
        if(i % 3 == 0):
            sum += y[i]*2
        else:
            sum+= y[i]*3
    return (3*sum*h)/8

x_data = [0, 1/6, 1/3, 1/2, 2/3, 5/6, 1]
y_data = [1, 0.9729, 0.9, 0.8, 0.6923, 0.59016, 1/2]
result = simpsons3by8(x_data,y_data)
print(result)

