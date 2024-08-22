nBin = list(input('Binário: '));
nBin.reverse(); #inverte a lista
tamanho = len(nBin);
decimal = 0

for i in range(tamanho):
    decimal = decimal + (nBin[i] * (2**i))

print(decimal)