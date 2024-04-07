import random
def function(x):
    return x**6 - x -1

def falsePositionMethod(tolerance,maxiter = 200,range = 2):
    j = 0
    while(function(j) * function(j+1))>0:
        j+=1
    a = j
    b = j + 1
    c = (a*function(b) - b*function(a))/function(b)-function(a)
    prev_c = None
    iter = 0
    while iter <= maxiter:
        prev_c = c
        if function(c>0):
            a = c
        else:
            b = c
        c = (a*function(b) - b*function(a))/(function(b)-function(a))
        iter+=1
        print("Iteration: ",iter)
        print("a: ",a)
        print("b: ",b)
        print("c: ",c)
        print("f(c): ",function(c))
        if (abs(c-prev_c)<=tolerance):
            break
    return c
    

c =  falsePositionMethod(0.0005)
print(c)



