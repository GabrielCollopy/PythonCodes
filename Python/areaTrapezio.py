B = input("Informe a base maior: ").replace(",",".")
while True:
    try:
        B = float(B)
        if B >= 0:
            break
        else:
            print("O valor inserido precisa ser maior do que 0.")
            B = input("Informe a base maior: ").replace(",",".")
    except:
        print("O valor digitado precisa ser um número: ")
        B = input("Informe a base maior: ").replace(",",".")

b = input("Informe a base menor: ").replace(",",".")
while True:
    try:
        b = float(b)
        if b > 0:
            if b < B:
                break
            else:
                print("O valor da base menor precisa ser menor que a base maior.")
                b = input("Informe a base menor: ").replace(",",".")
    except:
        print("O valor digitado precisa ser um número.")
        b = input("Informe a base menor: ").replace(",",".")

h = input("Informe a altura: ").replace(",",".")
while True:
    try:
        h = float(B)
        if h >= 0:
            break
        else:
            print("O valor inserido precisa ser maior do que 0.")
            h = input("Informe a altura: ").replace(",",".")
    except:
        print("O valor digitado precisa ser um número: ")
        h = input("Informe a base maior: ").replace(",",".")

print(f"A área do trapézio é {((B + b)*h)/2}cm².")