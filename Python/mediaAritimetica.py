'''
    Escrever um programa que leia um número não determinado de valores e
    calcule a média aritimética dos valores lidos, a quantidade de valores
    positivos, a quantidade de valores negativos e o percentual de valores
    negativos e positivo.
    Mostre os resultados.
    Crie uma função, em sua biblioteca de funções, que garanta que
    apenas números inteiros sejam digitados.
'''
print('')
print(f'{"Média Aritimética Inteiros Mk.1".center(61)}')
print('-='*30+'-')
print('')

import biblioteca

somaTotal = 0
contarTotal = 0
contarPos = 0
contarNeg = 0

print("Digite '0' para finalizar o programa.")
valor = biblioteca.verInt("Digite um número inteiro: ")

while valor != 0:
    
    somaTotal += valor
    contarTotal += 1
    if valor > 0:
        contarPos += 1
    else:
        contarNeg += 1
    
    print("Digite '0' para finalizar o programa.")
    valor = biblioteca.verInt("Digite um número inteiro: ")

if contarTotal > 0:
    mediaTotal = somaTotal/contarTotal
    porcentoPos = (contarPos/contarTotal) * 100
    porcentoNeg = (contarNeg/contarTotal) * 100

    print('-='*30+'-')
    print("")
    print(f"A média aritimética total dos números é {mediaTotal:.2f}.")
    print(f"A quantidade total de números positivos é {contarPos}.")
    print(f"A quantidade total de números negativos é {contarNeg}.")
    print(f"A porcentagem dos números positivos é {porcentoPos:.2f}% e a dos números negativos é {porcentoNeg:.2f}%.")
else:
    print("Nenhum valor inserido!")