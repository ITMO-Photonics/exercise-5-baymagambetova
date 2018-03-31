import numpy as np
# define a custom-build root-finding function (e.g. the one discussed in Lecture 1)
def f(x):
    return (x-3.)*(x*x+1.)
a=0.
b=7.
tolerance=1.e-3

if( f(a)*f(b)>0. ):
    print('Error: f(a) and f(b) should have opposite signs! Stopping.')
else:
    while(0.5*(b-a) > tolerance):
        c = 0.5*(a+b)
        if( f(a)*f(c)<0. ):
            b=c
        else:
            a=c    
    print('result: ',0.5*(b+a))

x=np.linspace(0.,5.,100)

import scipy
from scipy import optimize
x_bisect = scipy.optimize.bisect (f,a,b)
x_newton = scipy.optimize.newton (f,a)
x_brentq = scipy.optimize.brentq (f,a,b)
print(x_bisect, x_newton, x_brentq)

