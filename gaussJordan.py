def jordan(a,b):
    n = len(b)
    # Proses Eliminasi segitiga bawah
    for i in range(1,n):
        for j in range(0,n):
            if(i == j or i < j) : continue
            #print(i,j)
            if a[i,j] != 0.0:
                lam = a[i,j]/a[j,j]
                a[i,j:n] = a[i,j:n] - lam*a[j,j:n]
                b[i] = b[i] - lam*b[j]
            if (a[i,j] > -1.0e-6 and a[i,j] < 1.0e-6 ):
                a[i,j] = 0

    # Proses Eliminasi segitiga atas
    for i in reversed(range(0,n-1)):
        for j in reversed(range(i+1,n)):
            if a[i,j] != 0.0:
                lam = a[i,j]/a[j,j]
                a[i,j:n] = a[i,j:n] - lam*a[j,j:n]
                b[i] = b[i] - lam*b[j]
            if (a[i,j] > -1.0e-6 and a[i,j] < 1.0e-6 ):
                a[i,j] = 0      

    # Proses Diagonalisasi
    for i in range(0,n):
        for j in range(0,n):
            if(a[i,i] != 1):
                b[i] /= a[i,i]
                a[i,i] /= a[i,i]
    return b