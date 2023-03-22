import sympy as sym #our package to replicate/replace maple
eval = lambda f,val : f.evalf(subs={x:val}) #this function serves to reduce the clutter of my code. It evaluates a function for a given value of x.


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



if __name__ == '__main__': #Our __main__ function is as follows:
    
    x = sym.Symbol('x') # establishing x as a variable.
    #Use the Bisection method to find solutions accurate to within 10E−2 for x^4 − 2x^3 − 4x^2 + 4x + 4 = 0 on each interval.
    f4 = x**4 - 2*x**3 - 4*x**2 + 4*x +4
    f4a = bisection(f4, -2, -1, 10**-2) # a: [-2,-1]
    f4b = bisection(f4, 0, 2, 10**-2) # b: [0,2]
    f4c = bisection(f4, 2, 3, 10**-2) # c: [2,3]
    f4d = bisection(f4, -1, 0, 10**-2) # d: [-1,0]
    # #7a: Sketch the graphs of y = x and y = 2 sin x.
    f7 = 2*sym.sin(x)
    xyBounds = (-2.5, 2.5) #defining the lower and upper limits for plotting on the next line.
    sym.plotting.plot(x, f7, xlim = xyBounds, ylim = xyBounds, title="y = x & y = 2sin(x)") # plotting y=x and y=2sin(x) between -2.5,2.5 in x and y
    # #7b: Use the Bisection method to find an approximation to within 10E−5 to the first positive value of x with x = 2 sin x.
    f7b = bisection(f7-x, 0+10**-10, 2, 10**-5)
    # #14: Use Theorem 2.1 to find a bound for the number of iterations needed to achieve an approximation with accuracy 10−3 to the solution of x3 +x−4 = 0 lying in the interval [1, 4].
    # Find an approximation to the root with this degree of accuracy.
    f_14 = x**3 + x - 4
    f14 = bisection(f_14, 1, 4, 10**-3, countOut=True)

    
    
    
    
    #Outputting the answers
    try:
        print("#4: Let f(x) = {0}, f(x) = 0\n a) {1} when x ∈ [-2,-1] \n b) {2} when x ∈ [0,2] \n c) {3} when x ∈ [2,3] \n d) {4} when x ∈ [-1,0]".format(f4, f4a, f4b, f4c, f4d))
    except:
        print("#4: Let f(x) = {0}, f(x) = 0\n a) {1} when x in [-2,-1] \n b) {2} when x in [0,2] \n c) {3} when x in [2,3] \n d) {4} when x in [-1,0]".format(f4, f4a, f4b, f4c, f4d))
        #CLI doesn't enjoy the '∈' symbol. Controlling for that.
    print(f"#7b: Let f(x) = {f7b} = x. f(x)-x = 0 when x = {f7b}.")
    print(f"#14: Let f(x) = {f_14}. f(x) = 0 when x = {f14[0]}. This was found in {f14[1]} iterations.")
    
    
# def eval(f,var): 
#this function serves to reduce the clutter of my code.
#     return f.evalf(subs={x:var})