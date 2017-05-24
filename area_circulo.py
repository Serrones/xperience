# Capítulo 02 do livro Pense Allen

from math import pi



def area(r):
    return pi * r**2

def volume(r):
    return (3 / 4) * pi * r**3

r = float(input('Favor digitar o raio do círculo: '))

print('A área do círculo é de %.2f cm2 ' %area(r))
print('O volume do círculo é de %.2f cm3' %volume(r))
