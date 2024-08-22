soma = int(0)
vetor =[]

for i in range(20):
    num = int(input('Digite um número: '));
    vetor.append(num);

for j in vetor[:10]:
    soma += j

print('A soma dos 10 primeiros números é:',soma)
