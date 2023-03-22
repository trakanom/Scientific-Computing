import sympy as sym
x = sym.Symbol('x')
eval = lambda f,val : f.evalf(subs={x:val})


def hermite_interpolation(elems):
    dubm_varjaiblessssss = {
        'x':[],
        'fx':[],
        'dfdx':[]
    }
    for elem in elems:
        dubm_varjaiblessssss['x'].append(elem[0])
        dubm_varjaiblessssss['fx'].append(elem[1])
        dubm_varjaiblessssss['dfdx'].append(elem[2])
    
    print(dubm_varjaiblessssss)
    dubm_outpoots = {
        
    }

    for i in range(len(dubm_varjaiblessssss['x'])):
        pass
    
    


prob_2a = [[0, 1,2], [0.5, 2.71828, 5.43656]]
prob_2b = [[-0.25, 1.33203, 0.437500], [0.25, 0.800781, -0.625]]
prob_2c = [[0.1, -0.29004996, -2.8019975], [0.2, -0.56079734, -2.6159201], [0.3, -0.81401972, -2.9734038]]
prob_2d = [[-1, 0.86199,0.15536240] ,[-0.5, 0.95802009, 0.23269654], [0, 1.0986123, 0.3333333], [0.5, 1.2943767, 0.4516776]]

hermite_interpolation(prob_2a)
hermite_interpolation(prob_2b)
hermite_interpolation(prob_2c)
hermite_interpolation(prob_2d)


# p = sym.plotting.plot(f2, f2a, f2b, x, xlim = (0,5), ylim = (-1,5), title="Activity 2 #2", show=False)
# p[0].line_color = 'r'
# p[2].line_color = 'g'
# p[3].line_color = 'y'
# p.show()



