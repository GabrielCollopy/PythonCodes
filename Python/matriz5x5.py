matriz = []
vetor = []
soma = 0

for i in range(5): #começa a percorrer para inserir os valores na lista
    temp = [] # lista temporária
    for j in range(5): # insere os valores na lista, ao chegar a 5, inicia novamente e cria uma nova lista
        temp.append(int(input(f"Digite o {j+1}° valor para a {i+1}° linha da matriz: ")))
    matriz.append(temp)


for i in matriz:
    for j in i:
        for k in j:
            soma += k
vetor.append(soma)



print(vetor)
print("")
for i in matriz:
    print(i)
