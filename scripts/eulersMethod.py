def func( x, y ):
    return (x + y )

def eulersMethos(x0,y,x,step_size = 10):
    h = (x-x0)/step_size
    while x0<=x:
        y = y + h*func(x0,y)
        x0 = x0 + h
    print("Approximate solution at x = ", x, " is ", "%.6f"%y)
    return x0

x0 = 0
y0 = 1
h = 0.025
x = 0.1
 
result=eulersMethos(x0, y0, x)
