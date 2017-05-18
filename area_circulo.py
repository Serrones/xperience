# area de um circulo

import math

def area(r):
    a = math.pi * r**2
    return a

r = input('Favor digitar o raio do circulo: ')
r = int(r)

x = area(r)

print('A area do circulo e de: ', x)
