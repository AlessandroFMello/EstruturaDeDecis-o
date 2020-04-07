import msvcrt

while True:
    numero = float(input('Digite um número:\n').replace(',', '.'))

    if numero // 1 == numero:
        print('O número %s é inteiro!' % numero)
    else:
        print('O número %s é decimal!' % numero)

    print('\nPressione qualquer tecla para continuar ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
