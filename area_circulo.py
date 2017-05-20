# area de um circulo

import math

def area(r):
    return math.pi * r**2

r = int(input('Favor digitar o raio do circulo: '))

print('A area do circulo e de: %.2f ' %area(r))
