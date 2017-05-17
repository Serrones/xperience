# Contagem_Regressiva

def cronometro(num):
    if num <= 0:
        print('Boom!')
    else:
        print(num)
        cronometro(num-1)


# n = input('Favor digitar um número: ')

# num = int(n)

cronometro(int(input('Favor digitar um número')))
