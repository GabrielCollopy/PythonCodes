lista = [[1,2,3],
         [4,5,6],
         [7,8,9]]
#MATRIZ
# 3 linhas
# 3 colunas


# Percorrer a matriz

for i in lista: #linha
    for j in i: #coluna
        print(j,end=" ") # não pula linha no final da frase

#pausar e fechar a janela
input("")
quit()