import error
from numpy import sign

def falsePos(f,xl,xu,tol=1.0e-9):
    fl = f(xl)
    if fl == 0.0: return xl
    fu = f(xu)
    if fu == 0.0: return xu
    if sign(fl) == sign(fu):
        error.err('erorr yaa')
    xr = 0.0
    for i in range(100):
        xrold = xr
        xr = xu - (fu*(xl-xu))/(fl-fu)
        fr = f(xr)
        if (fr==0.0 or abs(xrold-xr)<tol): return xr
        if sign(fu) != sign(fr):
            xl = xr;fl=fr
        else:
            xu=xr;fu=fr