import msvcrt
while True:
    combustivel = input('Você vai abastecer álcool(A) ou gasolina(G)?\n')
    quantidade = float(input('Quantos litros?\n').replace(',', '.'))

    alcool = 1.9
    gasolina = 2.5
    preço = 0

    while combustivel == 'A' or combustivel == 'a' or combustivel == 'Álcool' or combustivel == 'álcool':
        combustivel = 'álcool'
        if quantidade <= 20:
            preço = (alcool * quantidade) * 0.97
            break
        elif quantidade > 20:
            preço = (alcool * quantidade) * 0.95
            break
        else:
            preço = input('Quantos reais quer abastecer de álcool?\n')
            break

    while combustivel == 'G' or combustivel == 'g' or combustivel == 'Gasolina' or combustivel == 'gasolina':
        combustivel = 'gasolina'
        if quantidade <= 20:
            preço = (gasolina * quantidade) * 0.96
            break
        elif quantidade > 20:
            preço = (gasolina * quantidade) * 0.94
            break
        elif quantidade == 'N' or quantidade == 'n':
            preço = input('Quantos reais quer abastecer de gasolina?\n')
    print('\nO preço total a ser pago por %sL de %s é: R$%s' %
          (quantidade, combustivel, round(preço, 2)))

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair\n')
    command = msvcrt.getch()
    if command == b'1':
        break
