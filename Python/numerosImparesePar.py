somaImpar = 0;
contImpar = 0;
contPar =0;

for i in range (13):
    num = int(input("Digite um número inteiro: "));
    if num % 2 != 0:
        somaImpar += num
        contImpar += 1
    else:
        contPar += 1

print('A soma dos números ímpares digitados é:',somaImpar,', a quantidade de números ímpares digitados foi',contImpar,'e a quantidade de números pares digitados foram',contPar);