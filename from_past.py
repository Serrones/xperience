# from 70's to nowadays

import time

print(time.time())

seg = time.time()

minu = seg / 60
seg_sobra = seg % 60
seg_sobra = int(seg_sobra)

hr = minu / 60
hr = int(hr)
min_sobra = minu % 60
min_sobra = int(min_sobra)

dia = hr / 24
dia = int(dia)
hr_sobra = hr % 24
hr_sobra = int(hr_sobra)

print('Estamos no ar desde Primeiro de Janeiro de 1970, ou seja:', dia ,'dias,',
 hr_sobra ,'horas,', min_sobra ,'minutos e', seg_sobra ,'segundos!!'  )
