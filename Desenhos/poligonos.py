# Capítulo 04 do livro PenseAllen


import turtle

bob = turtle.Turtle()


def desenhar(t,length,n):
    ang = 360 / n
    for i in range(n):
        t.fd(length)
        t.rt(ang)

"""
desenhar(bob,100,8)

turtle.mainloop()
"""
