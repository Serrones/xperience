# Calculadora com funcoes

def mais(a,b):
    a = int(a)
    b = int(b)
    soma = a + b
    print('A soma de', a, 'e', b, 'é',soma)

def subtrai(a,b):
    a = int(a)
    b = int(b)
    menos = a - b
    print('A subtração de', a, 'por', b, 'é',menos)

def multiplica(a,b):
    a = int(a)
    b = int(b)
    vezes = a * b
    print('A multiplicação de', a, 'por', b, 'é',vezes)

def divide(a,b):
    a = int(a)
    b = int(b)
    divisao = a / b
    print('A divisão de', a, 'por', b, 'é',divisao)

def decide(decisao):
    if decisao == 'sair':
        print('Obrigado por utilizar esta humilde calculadora')
    else:
        if decisao == 'add':
            a = input('Digite o primeiro numero:')
            b = input('Digite o segundo numero:')
            mais(a,b)
            decisao = input('O que você deseja fazer:')
            decide(decisao)
        else:
            if decisao == 'sub':
                a = input('Digite o primeiro numero:')
                b = input('Digite o segundo numero:')
                subtrai(a,b)
                decisao = input('O que você deseja fazer:')
                decide(decisao)
            else:
                if decisao == 'mult':
                    a = input('Digite o primeiro numero:')
                    b = input('Digite o segundo numero:')
                    multiplica(a,b)
                    decisao = input('O que você deseja fazer:')
                    decide(decisao)
                else:
                    if decisao == 'div':
                        a = input('Digite o primeiro numero:')
                        b = input('Digite o segundo numero:')
                        divide(a,b)
                        decisao = input('O que você deseja fazer:')
                        decide(decisao)
                    else:
                        print('\n---------Comando não reconhecido------------\n')
                        decisao = input('O que você deseja fazer:')
                        decide(decisao)



print('Olá amiguinho!! \n\nAbaixo estão os comandos da calculadora:\n\n\nSair da calculadora: sair\nAdição: add\nSubtração: sub \nMultiplicação: mult\nDivisão: div\n' )

decisao = input('O que você deseja fazer:\n')

decide(decisao)
