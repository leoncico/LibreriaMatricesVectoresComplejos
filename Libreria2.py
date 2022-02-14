import Libreria1 as lc
import math

#Adición de Vectores Complejos.
def adicionvec(v,w):
    tamano = len(v)
    suma = [[lc.sumacplx(v[j][0], w[j][0])] for j in range(tamano)]
    return suma

#Inverso de un Vector Complejo
def invvector(v):
    tamano=len(v)
    inv = [[(-1*v[i][0][0],-1*v[i][0][1])]for i in range(tamano)]
    return inv

#Multiplicación de un escalar por un vector complejo
def multesc_vec(c,w):
    tamano=len(w)
    mult=[(c*w[i][0][0], c*w[i][0][1]) for i in range(tamano)]
    return mult

#Adición de matrices complejas
def sumamatriz(A,B):
    columnas = len(A[0])
    filas = len(A)
    m = []
    for i in range(filas):
        f = []
        for j in range(columnas):
            f = f + [(lc.sumacplx(A[i][j], B[i][j]))]
        m = m + [f]
    return m

#Inversa aditiva de una matriz compleja
def invadmatriz(A):
    m = []
    for i in range(len(A)):
        f = []
        for j in range(len(A[0])):
            f = f + [(-1*A[i][j][0] , -1*A[i][j][1])]
        m = m + [f]
    return m

#Multiplicación de un escalar por una matriz compleja
def multesc_matriz(c, A):
    m = []
    for i in range(len(A)):
        f = []
        for j in range(len(A[0])):
            f = f + [(c*A[i][j][0],c*A[i][j][1])]
        m = m + [f]
    return m

#Traspuesta de una matriz/vector
def trasp(A):
    f = len(A)
    c = len(A[0])
    m = [[0 for i in range(f)]for i in range(c)]
    for i in range(f):
        for j in range(c):
            m[j][i] = (A[i][j])
    return m

#Conjugada de una matriz/vector
def conjug(A):
    m = []
    for i in range(len(A)):
        f = []
        for j in range(len(A[0])):
            f = f + [(lc.conjugadocplx(A[i][j]))]
        m = m + [f]
    return m

#Adjunta de una matriz/vector
def adj(A):
    m = []
    for i in range(len(A)):
        f = []
        for j in range(len(A[0])):
            f = f + [lc.conjugadocplx(A[i][j])]
        m = m + [f]
    return trasp(m)

#Producto de dos matrices (de tamaños compatibles)
def productomatrices(A, B):
    f = len(A)
    c = len(A[0])
    m = []
    for i in range(f):
        fila = []
        for j in range(f):
            suma = (0,0)
            for k in range(c):
                suma = lc.sumacplx(suma, lc.productocplx(A[i][k], B[k][j]))
            fila += [suma]
        m += [fila]
    return m

#Acción de una matriz sobre un vector
def accmatriz_vector(A, B):
    m = len(A)
    n = len(A[0])
    f = [(0, 0)] * n
    r = [f] * m
    for j in range(m):
        f = [(0, 0)] * n
        r[j] = f
        for k in range(n):
            r[j][k] = lc.productocplx(A[j][k], B[j][k])
    return r

#Producto interno entre vectores
def productointerno(A, B):
    for i in range(len(A)):
        A[i][0] = lc.conjugadocplx(A[i][0])
    f = len(A)
    m = [0 for i in range(f)]
    for i in range(f):
        m[i] = A[i][0]
    suma = (0,0)
    for i in range(len(m)):
        suma = lc.sumacplx(suma, lc.productocplx(m[i], B[i][0]))
    return suma

#Norma de un vector
def norma_vector(v):
    res = productointerno(v,v)
    return math.sqrt(abs(res[0]))

#Distancia entre dos vectores
def distvectores(A, B):
    suma = adicionvec(A, invvector(B))
    return norma_vector(suma)

#Revisar si la matriz es unitaria
def matrizunitaria(A):
    f = len(A)
    c = len(A[0])
    if f != c:
        return "La matriz no es unitaria"
    B = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila = fila + [lc.conjugadocplx(A[i][j])]
        B = B + [fila]
    m = [[0 for i in range(f)]for i in range(c)]
    for i in range(f):
        for j in range(c):
            m[j][i] = B[i][j]
    unitaria = []
    for i in range(f):
        fila = []
        for j in range(c):
            suma = (0,0)
            for k in range(f):
                suma = lc.sumacplx(suma, lc.productocplx(A[i][j], B[j][k]))
            f += [suma]
        unitaria += [f]
    for i in range(f):
        for j in range(c):
            if i == j:
                if unitaria[i][j] != 1:
                    return "La matriz no es unitaria"
            else:
                if unitaria[i][j] != 0:
                    return "La matriz no es unitaria"
    return "La matriz es unitaria"

#Revisar si la matriz es Hermintiana
def matrizherm(A):
    f = len(A)
    c = len(A[0])
    if f != c:
        return "La matriz no es hermitiana"
    B = [[0 for i in range(f)]for i in range(c)]
    for i in range(f):
        for j in range(c):
            B[j][i] = A[i][j]
    for i in range(f):
        for j in range(c):
            B[i][j] = lc.conjugadocplx(B[i][j])
    for i in range(f):
        for j in range(c):
            if B[i][j] != A[i][j]:
                return "La matriz no es hermitiana"
    return "La matriz es hermitiana"



if __name__ == '__main__':
    print(adicionvec([ [(1,2)],[(9,3)]],[[(9,8)],[(1,0)]]))
    print(invvector([ [(1,2)],[(-3,-5)]]))
    print(multesc_vec(2,[[(1,8)],[(-5,1)]]))
    print(sumamatriz([ [(1,1),(2,2)],[(3,3),(4,4)] ],[ [(1,1),(2,2)],[(3,3),(4,4)] ] ))
    print(invadmatriz([[ (1,8),(3,-8)]]))
    print(multesc_matriz(2,[ [(1,1),(2,2)],[(3,3),(4,4)] ]))
    print(trasp([ [(1,1),(2,2)],[(3,3),(4,4)] ]))
    print(conjug( [ [(1,1),(2,2)],[(3,3),(4,4)] ] ))
    print(adj( [ [(1,1),(2,2)],[(3,3),(4,4)] ] ))
    print(productomatrices([ [(1,1),(2,2)],[(3,3),(4,4)] ],[ [(1,1),(2,2)],[(3,3),(4,4)] ]))
    print(accmatriz_vector([ [(2,-3),(1,1)] ], [[(1,1),(2,2)],[(3,3),(4,4)]] ))
    print(productointerno( [[(1,0)]],[[(1,0)]]))
    print(norma_vector([[(5,10),(10,15)]]))
    print(distvectores( [[(1,2)],[(9,3)] ],[[(9,8)],[(1,0)] ]))
    print(matrizunitaria([ [(0,1),(0,1)]]))
    print(matrizherm([ [(5,0),(3,7)],[(3,-7) , (2,0) ] ]))