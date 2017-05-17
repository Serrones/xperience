def numero():
    num1 = input('Favor digitar um número: ')
    num2 = input('Favor digitar outro número: ')
    soma = int(num1) + int(num2)
    return soma

total = numero()

print('Total é: ', total,'Tipo: ', type(total))
