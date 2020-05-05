import numpy as np
import math
def conjGrad(A,x,b,N,tol=1.0e-6):
    r = b - A.dot(x)
    p = r.copy()
    for i in range(N-1):
        Ap = A.dot(p)
        alpha = np.dot(p,r)/np.dot(p,Ap)
        x = x + alpha*p
        r = b - A.dot(x)
        if math.sqrt(np.sum((r**2))) < tol:
            print('Itr:', i)
            break
        else:
            beta = -np.dot(r,Ap)/np.dot(p,Ap)
            p = r + beta*p
    return x 