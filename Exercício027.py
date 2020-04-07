import msvcrt

while True:
    quantMor = float(
        input('Quantos quilos de morango você quer?\n').replace(',', '.'))
    quantMaç = float(
        input('Quantos quilos de maçã você quer?\n').replace(',', '.'))

    if quantMor <= 5:
        pMorango = 2.5
    elif quantMor > 5:
        pMorango = 2.2

    if quantMaç <= 5:
        pMaçã = 1.8
    elif quantMaç > 5:
        pMaçã = 1.5

    total = (quantMor * pMorango) + (quantMaç * pMaçã)

    if total > 25 or (quantMor + quantMaç) > 8:
        total = total * 0.9

    print('O preço total a ser pago por %sKg de morango mais %sKg de maçã é: R$%s' %
          (quantMor, quantMaç, round(total, 2)))

    print('\nPressione qualquer tecla para continuar ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
