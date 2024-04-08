import random
def function(x):
    return x**6 - x -1

def d_f(x):
    return 6*x**5 - 1

def newtonRaphsonMethod(tolerance,maxiter = 200,range = 2):
    j = 0
    while(function(j) * function(j+1))>0:
        j+=1
    a = j
    b = j + 1
    c = random.uniform(0.5,range)
    denom = d_f(c)
    if denom == 0:
        e = 2
        return
    prev_c = None
    iter = 0
    while iter <= maxiter:
        prev_c = c
        denom = d_f(c)
        if denom == 0:
            e = 2
            break
        c = prev_c - function(prev_c)/denom
        if (abs(c-prev_c)<=tolerance):
            break
        iter+=1
        print("Iteration: ",iter)
        print("a: ",a)
        print("b: ",b)
        print("c: ",c)
        print("f(c): ",function(c))
    return c

c=newtonRaphsonMethod(0.0005)
print(c)

