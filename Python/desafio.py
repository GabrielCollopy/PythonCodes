import random

arquivo = open("nomes.txt", "r")

with open("nomes.txt", "r") as arquivo:
    nomes = arquivo.read().splitlines()
    vencedores = []
    selecionado = " "

while len(vencedores) < 3:
    selecionado = random.choice(nomes)
    if selecionado not in vencedores:
        vencedores.append(selecionado)

print(f"Vencedores: \n1-{vencedores[0]} \n2-{vencedores[1]} \n3-{vencedores[2]}")
