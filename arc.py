# Capítulo 4 livro PenseAllen

# circun = 2 * pi * r

#Criação de Pacote, e import de módulo

from math import pi

import turtle

import Desenhos

bob = turtle.Turtle()

def circle(t,r,angle):
    circun = 2 * pi * r
    n = int(circun / 3) + 1
    length = circun / n
    Desenhos.desenhar(t,length,n)

circle(bob,100,360)

turtle.mainloop()
