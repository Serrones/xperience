# from 70's to nowadays

from time import time

print(time(),'segundos')

seg = time()

minu = seg // 60
seg_sobra = int(seg % 60)

hr = minu // 60
min_sobra = int(minu % 60)

dia = int(hr / 24)
hr_sobra = int(hr % 24)

print('Estamos no ar desde Primeiro de Janeiro de 1970,',
      'ou seja: {} dias, {} horas, {} minutos e {} segundos!!'.format(dia,hr_sobra,min_sobra,seg_sobra))
