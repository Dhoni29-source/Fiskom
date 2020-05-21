import numpy as np
from midpoint import *
def bulStoer(F,x,y,xStop,H,tol=1.0e-6):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xStop:
        H = min(H,xStop - x)
        y = integrate(F,x,y,x + H,tol) # Midpoint method
        x=x+H
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y)