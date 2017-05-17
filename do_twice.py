"""
Um objeto de função é um valor que pode ser atribuído a uma
variável ou passado como argumento. Por exemplo, do_twice é
uma função que toma um objeto de função como argumento e o
chama duas vezes

"""

def melhores_bandas():
    print('spam ')
    print('spam ')

def do_twice():
    melhores_bandas()
    melhores_bandas()

do_twice()
