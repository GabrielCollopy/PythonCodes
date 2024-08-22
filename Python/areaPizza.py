print('')
print(f'{"Área Pizza Mk.1".center(61)}')
print('-='*30+'-')
print('')

raioPizza = input('Informe o raio da Pizza em centímetros: ').replace(',','.')

valido = False

while not valido:
    try:
        raioPizza = float(raioPizza)
        valido = True
    except:
        print('Valor inserido não válido. Por favor inserir um novo valor.')
        raioPizza = input('Informe o raio da Pizza em centímetros: ').replace(',','.')

area = (raioPizza ** 2) * 3.14

print(f'A área dessa pizza será de {area:.2f}cm²')