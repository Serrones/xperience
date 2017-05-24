# utilizando o módulo turtle

import turtle
bob = turtle.Turtle()
print(bob)

for i in range(4):
    bob.fd(200)
    bob.lt(90)

bob.lt(45)
bob.fd(100)
bob.lt(45)

for i in range(4):
    bob.fd(200)
    bob.lt(90)

bob.fd(200)
bob.lt(135)
bob.fd(100)

turtle.mainloop()
