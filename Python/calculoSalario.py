print(f'{"Salário Calculator Mk.1".center(61)}')
print('-='*30+'-')

salario = input('Informe o seu salário: ').replace(',','.')

valido = False

while not valido:
    try:
        salario = float(salario)
        valido = True
    except:
        print('Valor inserido não válido. Por favor inserir um novo valor.')
        salario = input('Informe o seu salário: ').replace(',','.')

salarioAumento = 1.15 * salario
salarioDesconto = salarioAumento - (0.08 * salarioAumento) # ou salarioAumento * 0.92

print(f'O seu salário atual é R${salario:.2f}\nApós o aumento de 15% ele passará para R${salarioAumento:.2f}\nCom os descontos de 8% de impostos, o salário final fica R${salarioDesconto:.2f}')