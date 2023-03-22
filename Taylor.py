import numpy as np
import sympy as sym
from sympy.functions import exp
def Taylor(f, n, x0=0):
    diffs = [sym.factor(f)]
    taylor = []
    for i in range(1,n+1):
        diffs.append(sym.factor(sym.diff(diffs[-1])))
        # print()
    for order, funct in enumerate(diffs):
        result = funct.evalf(subs={x:x0},chop=True)
        print(f'P_{order}={funct}, P_{order}({x0})={result}')
        
    # print(*enumerate(diffs), sep="\n")
    return diffs
def eval(f,var):
    return f.evalf(subs={x:var})
def abs_error(f,x,p):
    return 

def bisection_iterative(funct,lower_bound,upper_bound, max_abs_error, n=None):
    n = 0 if n is None else n+1
    # a_n = funct.evalf(subs={x:lower_bound},chop=True)
    eval(funct, lower_bound)*eval(funct, upper_bound)
    # b_n = funct.evalf(subs={x:upper_bound},chop=True)
    if eval(funct, lower_bound)*eval(funct, upper_bound) <= 0:
        a_n = lower_bound
        b_n = upper_bound
        
        p_n = a_n+(b_n-a_n)/2
        fp_n = eval(funct, p_n)
    
    


def bisection(funct,lower_bound,upper_bound, max_abs_error, max_iterations=None):
    max_iterations = 10000 if max_iterations is None else max_iterations
    a_end = funct.evalf(subs={x:lower_bound},chop=True)
    b_end = funct.evalf(subs={x:upper_bound},chop=True)
    
    if a_end*b_end <= 0:
        a1 = lower_bound
        b1 = upper_bound
        p = None
        p1  = a1 + (b1-a1)/2
        fp = funct.evalf(subs={x:p1})
        counter=0
        while(abs(fp)>=max_abs_error and counter<max_iterations):
            if eval(funct,a1)*eval(funct,p1)>0:
                a1 = p1
                b1 = b1
            elif eval(funct,a1)*eval(funct,p1)<0:
                a1=a1
                b1=p1
            p1 = a1+(b1-a1)/2
            counter+=1
            fp = eval(funct,p1)
            print(f"p_{counter}=",fp)
        print(f'found {p1} in {counter} iterations')
        return p1
    else:
        print("Error, function does not cross zero along this interval.")
    
    pass
if __name__ == '__main__':
    x = sym.Symbol('x')
    #Below needs to be scraped
        # f0 = (x*sym.cos(x)-sym.sin(x))
        # f1 = x-sym.sin(x)
        # Taylor(f0,4,0)
        # Taylor(f1,4,0)
        # f1 = x**3 + 4*x**2 - 10
        # #Use the Bisection method to find solutions accurate to within 10E−2 for x^4 − 2x^3 − 4x^2 + 4x + 4 = 0 on each interval.
        # f4 = x**4 - 2*x**3 - 4*x**2 + 4*x +4
        # f4a = bisection(f4, -2, -1, 10**-2)
        # f4b = bisection(f4, 0, 2, 10**-2)
        # f4c = bisection(f4, 2, 3, 10**-2)
        # f4d = bisection(f4, -1, 0, 10**-2)
        # # #7a: Sketch the graphs of y = x and y = 2 sin x.
        # bounds = (-2.5, 2.5)
        # sym.plotting.plot(x, 2*sym.sin(x), xlim = bounds, ylim = bounds, title="y = x & y = 2sin(x)")
        # # #7b: Use the Bisection method to find an approximation to within 10E−5 to the first positive value of x with x = 2 sin x.
        # f7b = bisection(2*sym.sin(x)-x, 0.0000000000000000000001, 2, 10**-5)
        # # #14: Use Theorem 2.1 to find a bound for the number of iterations needed to achieve an approximation with accuracy 10−3 to the solution of x3 +x−4 = 0 lying in the interval [1, 4].
        # # Find an approximation to the root with this degree of accuracy.
        # f14 = bisection(x**3 + x - 4, 1, 4, 10**-4)
        
        
        # #Outputting the answers
        # print("#4: Let f(x) = {0}, f(x) = 0 t\n a) {1} when x ∈ [-2,-1] \n b) {2} when x ∈ [0,2] \n c) {3} when x ∈ [2,3] \n d) {4} when x ∈ [-1,0]".format(f4, f4a, f4b, f4c, f4d))
        # print(f"#5b: {f7b}")
    # print(f"#14: {f14}")
    
    g52 = 2 - (x**2) * sym.sin(x)
    a = sym.nsolve(g52, [-1,2], solver='bisect')
    b = bisection(g52, -1, 2, (10**(-6)))
    c = Taylor(g52, 3)
    print(a,b)
    # print(bisection(f1, 1,2, 10**-12))
    # print(sym.diff(f1))