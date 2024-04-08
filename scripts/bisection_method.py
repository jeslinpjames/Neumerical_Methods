def function(x):
    return x**6 - x -1

def bisectionMethod(fn, tolerance):
    prev_cn = 0
    iteration = 1
    j = 0
    while(fn(j)*fn(j+1)>0):
        j+=1
    a = j
    b = j+1
    while True:
        c = (a+b)/2
        fcn = fn(c)
        print(f"Iteration {iteration}:")
        print(f"  cn: {c}")
        print(f"  fn: {fcn}")
        print(f"  a: {a}")
        print(f"  b: {b}")
        if fcn>0:
            b = c
        else:
            a = c
        if (abs(c-prev_cn)<=tolerance):
            print("Converged at iteration =", iteration)
            break
        prev_cn = c
        iteration+=1
    return c

result = bisectionMethod(function,0.00005)
print(f"\nApproximate root: {result}")

        