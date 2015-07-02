from pprint import pprint
from operator import mul, add
from functools import reduce
import gmpy2

def dot(A, B):
    rows, cols = len(A), len(B[0])
    c = [[0 for j in range(cols)] for i in range(rows)]
    for row in range(rows):
        for column in range(cols):
            c[row][column] = reduce(
                add,
                map(
                    mul,
                    A[row],
                    [r[column] for r in B]
                )
            )
    return c

def pivotize(m):
    """Creates the pivoting matrix for m."""
    n = len(m)
    ID = [[gmpy2.mpq(i == j) for i in range(n)] for j in range(n)]
    for j in range(n):
        row = max(range(j, n), key=lambda i: abs(m[i][j]))
        if j != row:
            ID[j], ID[row] = ID[row], ID[j]
    return ID

def lu(A):
    """Decomposes a nxn matrix A by PA=LU and returns L, U and P."""
    n = len(A)
    L = [[gmpy2.mpq(0)] * n for i in range(n)]
    U = [[gmpy2.mpq(0)] * n for i in range(n)]
    P = pivotize(A)
    A2 = dot(P, A)
    for j in range(n):
        L[j][j] = gmpy2.mpq(1)
        for i in range(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in range(i))
            U[i][j] = A2[i][j] - s1
        for i in range(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in range(j))
            L[i][j] = (A2[i][j] - s2) /U[j][j]
    return L, U, P

if __name__ == '__main__':
    a = [
        [1, 3, 5],
        [2, 4, 7],
        [1, 1, 0],
    ]
    L, U, P = lu(a)

    pprint(L, width=40)
    print()
    pprint(U, width=40)
    print()
    pprint(P, width=40)
