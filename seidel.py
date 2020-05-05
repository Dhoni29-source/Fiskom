# Modul gaussseidel Tanpa relaksasi
import numpy as np
import math
def seidel(iterEqs,x,tol = 1.0e-9):
    k = 10
    p=1
    for i in range(1,501):
        xOld = x.copy()
        x = iterEqs(x)
        dx = math.sqrt(np.dot(x-xOld,x-xOld))
        if dx < tol: 
            return x,i
       