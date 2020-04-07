import msvcrt

while True:
    numero = int(input('Digite um número inteiro:\n'))

    if numero % 2 == 0:
        print('O número %s é par!' % numero)
    else:
        print('O número %s é ímpar!' % numero)

    print('\nPressione qualquer tecla para continuar ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
