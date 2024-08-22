lista1 = []
somaMatriz = 0

for i in range(3): #começa a percorrer para inserir os valores na lista
    temp = [] # lista temporária
    for j in range(3): # insere os valores na lista, ao chegar a 3, inicia novamente e cria uma nova lista
        temp.append(int(input(f"Digite o {j+1}° valor para a {i+1}° linha da matriz: ")))
    lista1.append(temp)

for i in lista1:
    for j in i:
        somaMatriz += j

for i in lista1:
    print(i)

print("")
print(somaMatriz)