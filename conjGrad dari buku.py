import numpy as np
import math
def conjGrad(Av,x,b,tol=1.0e-6):
    n = len(b)
    r = b - Av(x)
    s = r.copy()
    for i in r
    ange(n):
        u = Av(s)
        alpha = np.dot(s,r)/np.dot(s,u)
        x = x + alpha*s
        r = b - Av(x)
        if(math.sqrt(np.dot(r,r))) < tol:
            break
        else:
            beta = -np.dot(r,u)/np.dot(s,u)
            s = r + beta*s
    return x,i