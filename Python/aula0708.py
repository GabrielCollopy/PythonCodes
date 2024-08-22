import funcao # <-- Importa a biblioteca com o nome completo
#import funcao as fc <-- Importa a biblioteca a renomeando
#from funcao import decToBin <-- Importa uma única função da biblioteca

valor = input('Digite um número decimal: ')

convertido = funcao.decToBin(valor)

print(f'O número {valor} em binário é {convertido}!')