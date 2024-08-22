ipv4 = list(map(int,input('Insira o endereço IPv4:').split('.')))
binarios = []

for i in ipv4:
    octeto = bin(i + 256) [3:]
    binarios.append(octeto)

print('.'.join(binarios))