def pedir_numero():
    num = input('Por favor, digite um número: ')
    print('O número é: ' , num)
    return num


pilha = int(pedir_numero())

print('Tipo: ', type(pilha))
