# Calculadora com funcoes

def mais(a,b):
    soma = a + b
    print('A soma de {} e {} é {}\n\n\n'.format(a,b,soma))

def subtrai(a,b):
    menos = a - b
    print('A subtração de {} por {} é {}\n\n\n'.format(a,b,menos))

def multiplica(a,b):
    vezes = a * b
    print('A multiplicação de {} por {} é {}\n\n\n'.format(a,b,vezes))

def divide(a,b):
    divisao = a / b
    print('A divisão de {} por {} é {}\n\n\n'.format(a,b,divisao))

def menu():
    print('Abaixo estão os comandos da calculadora:\n\n',
      'Sair da calculadora: 0\nAdição: 1\nSubtração: 2 \nMultiplicação:',
      '3\nDivisão: 4\n')


def decide():
    decisao = input('O que você deseja fazer?\n')
    if decisao == '0':
        print('Obrigado por utilizar esta humilde calculadora')
    else:
        a = int(input('Digite o primeiro numero:'))
        b = int(input('Digite o segundo numero:'))
        if decisao == '1':
            mais(a,b)
        elif decisao == '2':
            subtrai(a,b)
        elif decisao == '3':
            multiplica(a,b)
        elif decisao == '4':
            divide(a,b)
        else:
            print('\n---------Comando não reconhecido------------\n\n\n')
    return decisao

print('Olá amiguinho!!')
decisao = ''
while decisao != '0':
    menu()
    decisao = decide()
