import sympy as sym
x = sym.symbols('x')
# f_14 = x**3 + x - 4
# f7 = 2*sym.sin(x)
# a = sym.nsolve(f_14, [1,4], solver='bisect') #using the built-in method.
# b = sym.nsolve(f7-x, (0, 2), solver='bisect')
# f= x**3 + 4*x**2 - 10
# c = sym.nsolve(f - x, [1,2], solver='bisect')
# d = sym.nsolve(f, [1,2], solver='bisect')

# e = f.evalf(subs={x:c})
# f = .5*(10 - x**3)**(.5)
# misc1 = f.diff(rational=True)
# m1a = misc1.evalf(subs={x:1})
# m1b = misc1.evalf(subs={x:1.5})
# print(misc1, m1a,m1b, sep="\n")
# print(c,d,e, sep="\n")
g52 = 2 - (x**2) * sym.sin(x)
a = sym.nsolve(g52, [-1,2], solver='bisect')
print(a)