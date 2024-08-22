erro = False;

'''Mapeia a váriavel para um valor inteiro'''
ip = list(map(int,input('Informe um endereço de IP: ').split(".")));
valido = True;

if len(ip) != 4:
    print('IP inválido!')
else:
    for i in ip:
        if i > 255 or i < 0:
            print('IP inválido -%d não é um valor de octeto possíve!'%i)
            valido = False

if valido:
    print('IP válido!')

'''Possível outra resolução:'''

''' octo1 = int(ip[0])
octo2 = int(ip[1])
octo3 = int(ip[2])
octo4 = int(ip[3])

if octo1 > 255 or octo1 < 0:
    erro = True;

if octo2 > 255 or octo2 < 0:
    erro = True;

if octo3 > 255 or octo3 < 0:
    erro = True;

if octo4 > 255 or octo4 < 0:
    erro = True;

if erro:
    print('IP inválido!')
else:
    print('IP válido!') '''