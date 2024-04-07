def fact(n):
    if n == 0:
        return 1
    fact = 1
    for i in range (2,n+1):
        fact*= i
    return fact

def cal(h,n):
    temp = h
    for i in range(1,n):
        temp = temp*(h-i)
    return temp


def newtonForwardInterpolation(x,y,value):
    n = len(x)
    p = (value-x[0])/(x[1]-x[0])
    
    for i in range(1,n):
        for j in range(n-i):
            y[j][i]= y[j+1][i-1] - y[j][i-1]
    sum =y[0][0]
    for i in range(1,n):
        print (fact(i),i)
        sum += (cal(p,i)*y[0][i])/ fact(i)
    return sum


x = [3, 5, 7, 9]
y = [[0 for _ in range(4)] for _ in range(4)]
y[0][0] = 180
y[1][0] = 150
y[2][0] = 120
y[3][0] = 90

value = 4
result = newtonForwardInterpolation(x, y, value)
print(f"Value at {value} is {result}")