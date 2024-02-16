import math

def formul(r,h):
    side = 2 * math.pi * r * h
    full = side + (2 * math.pi * r ** 2)
    return side, full


radius = int(input('Введите радиус: '))
high = int(input('Высота цилиндра: '))

side_cil, full_cil = formul(radius,high)
print('Площадь боковой поверхности: ', side_cil)
print('Полная площадь: ', full_cil)