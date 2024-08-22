from math import sqrt
from math import cos
from math import radians

print('')
print(f'{"Distância em Anos-Luz Mk.2".center(61)}')
print('-='*30+'-')
print('')

print(f"A distância entre KA-7 e KA-11 é {sqrt(1700**2 + 1200**2 - 2*1700 * 1200 * cos(radians(52))):.2f} anos-luz.")