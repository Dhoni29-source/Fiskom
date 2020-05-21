import numpy as np
def triangleQuad(f,xc,yc):
    alpha = np.array([[1/3, 1/3.0, 1/3], \
                    [0.2, 0.2, 0.6], \
                    [0.6, 0.2, 0.2], \
                    [0.2, 0.6, 0.2]])
    W = np.array([-27/48,25/48,25/48,25/48])
    x = np.dot(alpha,xc)
    y = np.dot(alpha,yc)
    A = (xc[1]*yc[2] - xc[2]*yc[1] \
        - xc[0]*yc[2] + xc[2]*yc[0] \
        + xc[0]*yc[1] - xc[1]*yc[0])/2.0
    sum = 0.0
    for i in range(4):
        sum = sum + W[i] * f(x[i],y[i])
    return A*sum