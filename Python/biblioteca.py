#conversor de binário para decimal
def binToDec (binario): 
    nBin = list(binario);
    nBin.reverse(); #inverte a lista
    tamanho = len(nBin);
    decimal = 0

    for i in range(tamanho):
        decimal = decimal + (int(nBin[i]) * (2**i))
    return(decimal)

#conversor de decimal para binário
def decToBin (decimal): 
    return bin(int(decimal))[2:]

#verificador de número inteiro
def verInt(texto):
    valido = False
    while not valido:
        try:
            num = input(texto).replace(",",".")
            num = float(num)
            num = int(num)
            valido = True
            return num
        except:
            print(f"O {num} não é um número inteiro.")