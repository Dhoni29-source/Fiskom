from functools import reduce
import operator

def lagrange(x, nilai_x, nilai_y):
    def dasar(j):
        p = [(x - nilai_x[m])/(nilai_x[j] - nilai_x[m]) for m in range(panjang_x) if m != j]
        return reduce(operator.mul, p)
    assert len(nilai_x) != 0 and (len(nilai_x) == len(nilai_y)) # nilai x & y tak boleh kosong dan harus memiliki panjang nilai yg sama
    panjang_x = len(nilai_x)
    return sum(dasar(j)*nilai_y[j] for j in range(panjang_x)) 
    
