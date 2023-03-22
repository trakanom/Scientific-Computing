'''
Section 2.2:
5. Use a fixed-point iteration method to determine a solution accurate to within 10−2 for x4−3x2−3 = 0 on [1, 2]. Use p0 =1.

8. Use Theorem 2.3 to show that g(x) = 2−x has a unique fixed point on [ 1 3 ,1]. Use fixed-point iteration
to find an approximation to the fixed point accurate to within 10−4. Use Corollary 2.5 to estimate the number of iterations required to achieve 10−4 accuracy, and compare this theoretical estimate to the
number actually needed.

16. Let A be a given positive constant and g(x) = 2x − Ax2. 
    a. Show that if fixed-point iteration converges to a nonzero limit, then the limit is p = 1/A,so the inverse of a number can be found using only multiplications and subtractions.
    b. Find an interval about 1/A for which fixed-point iteration converges, provided p0 is in that
    interval.
'''

'''
Section 2.3:
5. Use Newton’s method to find solutions accurate to within 10−4 for the following problems. 
    a. x3 − 2x2 − 5 = 0, 1[1, 4] 
    b. x3 + 3x2 − 1 = 0, [−3,−2] 
    c. x − cos x = 0,  [0, math.pi/2]
    d. x − 0.8 − 0.2 sin x = 0, [0, math.pi/2]
6. Use Newton’s method to find solutions accurate to within 10−5 for the following problems. 
    a. e^x + 2−x + 2 cos x − 6 = 0 for 1 ≤ x ≤ 2 
    b. ln(x − 1) + cos(x − 1) = 0 for 1.3 ≤ x ≤ 2
    c. 2x cos 2x − (x − 2)2 = 0 for 2 ≤ x ≤ 3 and 3 ≤ x ≤ 4 
    d. (x − 2)2 − ln x = 0 for 1 ≤ x ≤ 2 and e ≤ x ≤ 4 
    e. e^x − 3x2 = 0 for 0 ≤ x ≤ 1 and 3 ≤ x ≤ 5
    f. sin x − e−x = 0 for 0 ≤ x ≤ 13 ≤ x ≤ 4 and 6 ≤ x ≤ 7
15. The following describes Newton’s method graphically: 
    Suppose that f(x) exists on [a, b] and that f(x) != 0 on [a, b]. 
    Further, suppose there exists one p ∈[a, b] such that f( p) = 0, and let p0 ∈[a, b] be arbitrary. 
    Let p1 be the point at which the tangent line to f at ( p0, f( p0)) crosses the x-axis. 
    For each n ≥ 1, let pn be the x-intercept of the line tangent to f at ( p_n−1, f( p_n−1) ). 
    Derive the formula describing this method.
'''
import math
import sympy as sym
def inflection_pts(funct, max_diffs):
    print(funct)
    diff_dict = {
        "f(x)":funct
    }
    soln_dict = {}
    #https://docs.sympy.org/latest/modules/solvers/solveset.html
    for i in range(1, max_diffs+1):
        dict_index = "f"+"'"*(i%2) + '"'*(i//2) + "(x)"
        diff_dict[dict_index]=sym.diff(funct, x, i-1)
        print(f"{dict_index} = {diff_dict[dict_index]}")
        
        if diff_dict[dict_index]==0:
            break
    for diffs in diff_dict:
        # diff_dict[diffs]
        soln_dict[diffs] = sym.solveset(diff_dict[diffs], domain=sym.S.Reals)
        print(f"{diffs} = {diff_dict[diffs]} = {sym.solveset(diff_dict[diffs], domain=sym.S.Reals)}")
    print(sym.union(soln_dict.values()))
        
def bisection(funct,lower_bound,upper_bound, max_abs_error, max_iterations=None, printout=True, countOut = False):
    max_iterations = 10000 if max_iterations is None else max_iterations
    if eval(funct, lower_bound)*eval(funct, upper_bound) <= 0:
        a_n = lower_bound
        b_n = upper_bound
        p_n  = a_n + (b_n-a_n)/2
        fp = eval(funct,p_n)
        counter=0
        while(abs(fp)>=max_abs_error and counter<max_iterations):
            if eval(funct,a_n)*eval(funct,p_n)>0:
                a_n = p_n
                b_n = b_n
            elif eval(funct,a_n)*eval(funct,p_n)<0:
                a_n = a_n
                b_n = p_n
            p_n = a_n+(b_n-a_n)/2
            counter += 1
            fp = eval(funct,p_n)
        if printout:
            print(f"For x contained in [{lower_bound},{upper_bound}]:\n\t{funct} = 0 at x = {p_n}.\n\tFound in {counter} iterations.")
        return p_n if not countOut else [p_n, counter]
    else:
        print("Error, function does not cross zero along this interval.")
def fixedPoint(funct, p0, tolerance=None, max_iterations=None):
    max_iterations = 100 if max_iterations is None else max_iterations
    tolerance = 10**-6 if tolerance is None else tolerance
    print(tolerance)
    for i in range(max_iterations):
        p = eval(funct,p0)
        if abs(p - p0)<tolerance:
            print("done")
            return p
        else:
            print(i, p0, p, abs_dif(p,p0), abs_dif(p,p0)<tolerance,tolerance)
            p0=p
            
    print("errorstuff")
    return p0

if __name__ == '__main__':
    x = sym.Symbol('x')
    abs_dif = lambda a,b : abs(a-b)
    eval = lambda f,val : f.evalf(subs={x:val}) #this function serves to reduce the clutter of my code. It evaluates a function for a given value of x.
    f5a = x**4 - 3*x**2 - 3
    fff = (3*x**2 + 3)**(1/4)
    
    i5a = [1,2]
    # sym.plotting.plot(x, f5a, xlim = (-10,10), ylim = (-10,10), title="y = x & y = 2sin(x)")

    # f5a = x*3 - 2*x**2 - 5
    # i5a = [1, 4] 
    # f5b = x**3 + 3*x**2 - 1
    # i5b = [-3,-2]
    # f5c = x - sym.cos(x)
    # i5c = [0, math.pi/2]
    # f5d = x - 0.8 - 0.2*sym.sin(x)
    # i5d = [0, math.pi/2]

    # a = bisection(f5a, 1, 2, 10**-2)
    a = fixedPoint(funct=fff, p0=1, tolerance=10**-2)
    print(a)
    # print(a)
    # inflection_pts(fff,6)
    #https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fixed_point.html
    