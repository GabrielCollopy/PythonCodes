matriz = [[0 for _ in range(5) for _ in range(5)]]

for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Insira o valor para a posição {i} x {j}  da matriz."))