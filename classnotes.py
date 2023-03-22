#2-9-21
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = sym.Symbol('x')
    f = x**3 + 4*x**2-10
    # print(f, f.diff(), f.diff().diff(), sep="\n")
    bounds = lambda i: (-3.14*i, 3.14*(i+1))
    # sym.plotting.plot(f, xlim=bounds(10), ylim=bounds(10))
    print(sym.nsolve(f,bounds(100), solver='bisect', verify=False))
    