import sympy as sym
import math

def Lagrange_Interpolation(base_cases, degree, evalAt = None):
    L_n = [base_cases[j][1]*math.prod([(x - base_cases[k][0])/(base_cases[j][0]-base_cases[k][0]) if j!=k else 1 for k in range(degree+1)]) for j in range(degree+1)]
    P = sum(L_n)
    if evalAt!=None:
        try:
            ans = eval(P, evalAt)
            print(f"degree = {degree}, P={P.simplify()}, and P({evalAt}) = {ans}")
        except:
            print(f"It broke at degree = {degree}, but P({evalAt}) = {P}")                                 
    else:
        print(P)
#You can type latex in jupyter with a markdown cell!!! THANKS CYNTHIA

fdict = [
    [1.0, 0.7651977],
    [1.3, 0.6300860],
    [1.6, 0.4554022],
    [1.9, 0.2818186],
    [2.2, 0.1103623]
]
x = sym.Symbol('x')
eval = lambda f,val : f.evalf(subs={x:val})
# Lagrange_Interpolation(fdict, degree=0, evalAt=1.5)
# Lagrange_Interpolation(fdict, degree=1, evalAt=1.5)
# Lagrange_Interpolation(fdict, degree=2, evalAt=1.5)
# Lagrange_Interpolation(fdict, degree=3, evalAt=1.5)



print(sym.polys.polyfuncs.interpolate([(1.3, 0.6300860),(1.6, 0.4554022),(1.9, 0.2818186),(2.2, 0.1103623)],1.5))
