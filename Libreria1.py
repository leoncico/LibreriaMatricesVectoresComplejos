import math

def sumacplx(c1,c2):
    return (c1[0] + c2[0], c1[1] + c2[1])


def productocplx(c1,c2):
    real = ((c1[0] * c2[0]) - (c1[1] * c2[1]))
    img = ((c1[0] * c2[1]) + (c2[0] * c1[1]))
    return (real, img)


def restacplx(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])


def divisioncplx(c1, c2):
    real = ((c1[0] * c2[0]) + (c1[1] * c2[1])) / ((c2[0] ** 2) + (c2[1] ** 2))
    img = ((c1[1] * c2[0]) - (c1[0] * c2[1])) / ((c2[0] ** 2) + (c2[1] ** 2))
    return (real, img)


def modulocplx(c1):
    return (((c1[0] ** 2) + (c1[1] ** 2)) ** (1/2))


def conjugadocplx(c1):
    return (c1[0], (-c1[1]))


def conversion_polar_cartesianas(c1,P,angle):

    p = math.sqrt((((c1[0]) ** 2) + (c1[1] ** 2)))
    angle = math.atan((c1[1] / c1[0]))

    a = (P * math.cos(angle))
    b = (P * math.sin(angle))

    return f'Polares: {p, angle}', f'Cartesianas: {a,b}'

def fase(c1):
    angle = math.atan((c1[1] / c1[0]))
    return angle


if __name__ == '__main__':

    print ("Suma de complejos",sumacplx((3 , -1 ),(1 , 4 )))
    print ("Producto de complejos" , productocplx((8 , 2 ), (-5 , 1)))
    print ("Resta de complejos" , restacplx((-8 , 5), (1,5)))
    print ("Division de complejos" , divisioncplx((5.3,-2),(3.5,1)))
    print ("Modulo de complejos" , modulocplx((-6,13)))
    print ("Conjugado de un complejo" , conjugadocplx ((13 , 5)))
    print ("Conversion de polar a cartesianas" , conversion_polar_cartesianas((2,1), (math.sqrt(5)),(0.4636)))
    print ("Fase de un complejo" , fase((2,1)))