# Capítulo 02 do livro Pense Allen


"""
Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias
recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro
exemplar e 75 centavos para cada exemplar adicional.
Qual é o custo total de atacado para 60 cópias?
"""


def atacado(valor_livro,quant_livro):
    total = (valor_livro - (valor_livro * 0.4)) * quant_livro
    trans = 3 + ((quant_livro-1) * 0.75)
    return total + trans


quant_livro = int(input('Quantos livros você deseja comprar?\n'))
valor_livro = float(input('Qual o valor da unidade?\n'))

print('O total de despesas para %d livros é de %.2f' %(quant_livro,atacado(valor_livro,quant_livro)))


"""
Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo
(8min15s por quilômetro), então 3 quilômetros a um passo mais rápido
(7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro
lugar, que horas chego em casa para o café da manhã?
"""

t1 = ((8 * 60) + 15) * 2
t2 = ((7 * 60) + 12) * 3

tempo = (t1 + t2) / 60
cafe = ((6 * 60) + 52) + tempo
cafe = cafe / 60

print('Você chegará às %.2f'%cafe)
