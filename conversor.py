# Capítulo 01 do livro Pense Allen

print('\n1- Conversão de 42 minutos e 42 segundos para segundos')
seg = (42 * 60) + 42
print('Resposta: {} segundos'.format(seg))

print('\n2- Quantas milhas há em 10 quilômetros? (1 milha = 1.61 km)')
mil = 10 / 1.61
print('Resposta: Aproximadamente %.2f milhas'%mil)

print('\n3- Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual o\n'
      'passo médio em mlhas/minuto e milhas/segundo? E em milhas por hora?')
minuto = seg / 60
hora = minuto / 60
m_hor = mil / hora
m_min = mil / minuto
m_seg = mil / seg
print(' Passo médio em milhas/hora: %.2f m/h\n' %m_hor ,
      'Passo médio em milhas/minuto: %.2f m/m\n' %m_min,
      'Passo médio em mihas/segundo: %.4f m/s'%m_seg)
