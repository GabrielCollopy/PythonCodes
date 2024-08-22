print('')
print(f'{"Cálculo de Altura usando Seno Mk.1".center(61)}')
print('-='*30+'-')
print('')

'''
    Uma rampa plana, de 36m de comprimento, faz ângulo de 30° com o plano horizontal.
    Uma pessoa que suba a rampa inteira eleva-se, verticalmente, quantos metros?
'''

from math import sin
from math import radians
high = sin(radians(30)) * 36

print(f"A pessoa se elevou verticalmente {high:.2f} metros.")