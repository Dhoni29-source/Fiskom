import numpy as np
import math
def gaussSeidel(iterEqs,x,tol = 1.0e-6):
    omega = 1.0
    k = 10
    p=1
    for i in range(1,501):
        xOld = x.copy()
        x = iterEqs(x,omega)
        dx = math.sqrt(np.dot(x-xOld,x-xOld))
        if dx < tol: return x,i,omega
    # Compute relaxation factor after k+p iterations
    if i == k: dx1 = dx
    if i == k + p:
            dx2 = dx
            omega = 2.0/(1.0 + math.sqrt(1.0 \
                  - (dx2/dx1)**(1.0/p)))
