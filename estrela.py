# Capítulo 04 do livro PenseAllen


import turtle

bob = turtle.Turtle()

def estrela(t,length,n):
    ang = 135
    for i in range(n):
        t.fd(length)
        t.rt(ang)


estrela(bob,100,8)

sturtle.mainloop()
