from fractions import Fraction
from lu_decomp import lu, dot
from pprint import pprint
import gmpy2

def make_hilbert(dim=5):
    return [
        [
            gmpy2.mpq(1, i+j+1)
            for j in range(dim)
        ]
        for i in range(dim)
    ]

if __name__ == '__main__':
    with gmpy2.local_context(gmpy2.context(), precision=1000) as ctx:
        dim = 10
        Hilbert = make_hilbert(dim)

        L, U, P = lu(Hilbert)

        print(U[dim-1][dim-1])
        print(gmpy2.mpfr(U[dim-1][dim-1]))
