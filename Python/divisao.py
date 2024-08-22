print('')
print(f'{"Divisão de Números Mk.1".center(61)}')
print('-='*30+'-')
print('')

n1 = input('Informe o primeiro número: ')
n2 = input('Informe o segundo número: ')
div = 0

valido = False # Variável de controle ou FLAG.

while not valido: # verifica se os caracteres digitados são números.
    try:
        n1 == int(n1) or n2 == int(n2)
        valido = True # define uma variável de controle.
    except:
        print('Valores inseridos não válidos, favor informar outros valores') # caso não seja pede para o usuário inserir novamente.
        n1 = input('Informe o primeiro número: ')
        n2 = input('Informe o segundo número: ')

while valido == True:   # enquanto a variável for verdadeira, irá fazer os passos abaixo:
    if n2 > n1:
        print('Divisão não válida')
        n1 = input('Informe o primeiro número: ')
        n2 = input('Informe o segundo número: ')
    elif n2 == 0:
        print('Divisão por 0 não é possível')
        n1 = input('Informe o primeiro número: ')
        n2 = input('Informe o segundo número: ')
    else:
        n1 = int(n1)
        n2 = int(n2)
        div = n1/n2
        print(f'O resultado dessa divisão é {div:.2f}')
        valido = False

print('')
print('-='*30+'-')
input('Pressione ENTER para sair') # Espera a entrada do usuário para encerrar o programa.
quit()
