# verificar se é possível fazer um triângulo com 3 gravetos de tamanhos diferentes

def is_triangle():
    a = input('Favor digitar o tamanho do primeiro graveto, em centimetros:')
    b = input('Favor digitar o tamanho do segundo graveto, em centimetros:')
    c = input('Favor digitar o tamanho do terceiro graveto, em centimetros:')

    a = int(a)
    b = int(b)
    c = int(c)

    if a + b == c or b + c == a or a + c == b:
        print('Impossível formar um triangulo')
    else:
        print('Possivel formar um triangulo')


is_triangle()
