def numero():
    num1 = int(input('Favor digitar um número:\n'))
    num2 = int(input('Favor digitar outro número:\n'))
    soma = num1 + num2
    return soma

total = numero()
print('O total é {}, e o Tipo é {}'.format(total,type(total)))
