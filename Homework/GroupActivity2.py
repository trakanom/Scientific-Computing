import sympy as sym
x = sym.Symbol('x')
f2 = x**3 + 4*x**2 - 10
f2a = .5*(10-x**3)**(0.5)
f2b = x - (x**3 + 4*x**2 - 10)/(3*x**2 + 8*x)
p = sym.plotting.plot(f2, f2a, f2b, x, xlim = (0,5), ylim = (-1,5), title="Activity 2 #2", show=False)
p[0].line_color = 'r'
p[2].line_color = 'g'
p[3].line_color = 'y'
p.show()