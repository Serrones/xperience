# area de um circulo

from math import pi

def area(r):
    return pi * r**2

r = int(input('Favor digitar o raio do circulo: '))

print('A area do circulo e de: %.2f ' %area(r))
