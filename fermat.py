# Fermat

def check_fermat():
    tupla = ('Digite o primeiro número: ',
             'Digite o segundo número: ',
             'Agora, por favor digite o terceiro número: ',
             'Digite o último número: ')

    user = []
    for i in tupla:
        user.append(int(input(i)))

#    x = user[0]**user[3] + user[1]**user[3] == user[2]**user[3]
    a, b, c, n = user
    x = a**n + b**n == c**n

    if user[3] > 2 and x:
        print('Holy smokes, Fermat was wrong!!')
    else:
        print("No, that doesn't work", x )


check_fermat()
