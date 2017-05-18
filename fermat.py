# Fermat

def check_fermat():
    a = input('Favor digitar um numero:')
    b = input('Favor digitar outro numero:')
    c = input('Digite o terceiro numero:')
    n = input('E agora digite o ultimo numero:')

    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    x = a**n + b**n == c**n

    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!!')
    else:
        print("No, that doesn't work", x )
        

    return


check_fermat()
