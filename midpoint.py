import numpy as np
import math
def integrate(F,x,y,xStop,tol):
    def midpoint(F,x,y,xStop,nSteps):
        # Midpoint formulas
        h = (xStop - x)/nSteps
        y0 = y
        y1 = y0 + h*F(x,y0)
        for i in range(nSteps-1):
            x=x+h
            y2 = y0 + 2.0*h*F(x,y1)
            y0 = y1
            y1 = y2
        return 0.5*(y1 + y0 + h*F(x,y2))
    
    def richardson(r,k):
        # Richardson’s extrapolation
        for j in range(k-1,0,-1):
            const = (k/(k - 1.0))**(2.0*(k-j))
            r[j] = (const*r[j+1] - r[j])/(const - 1.0)
        return
    kMax = 51
    n = len(y)
    r = np.zeros((kMax,n))
    
#     Start with two integration steps
    nSteps = 2
    r[1] = midpoint(F,x,y,xStop,nSteps)
    r_old = r[1].copy()
    # Increase the number of integration points by 2
    # and refine result by Richardson extrapolation
    for k in range(2,kMax):
        nSteps = 2*k
        r[k] = midpoint(F,x,y,xStop,nSteps)
        richardson(r,k)
        # Compute RMS change in solution
        e = math.sqrt(np.sum((r[1] - r_old)**2)/n)
        # Check for convergence
        if e < tol: return r[1]
        r_old = r[1].copy()
    print("Midpoint method did not converge")