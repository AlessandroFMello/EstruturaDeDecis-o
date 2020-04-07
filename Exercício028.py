import msvcrt

while True:
    tipoCarne = input(
        'Escolha uma carne: Filé Duplo(F), Alcatra(A) ou Picanha(P)\n')

    if tipoCarne == 'f' or tipoCarne == 'F' or tipoCarne == 'Filé' or tipoCarne == 'filé' or tipoCarne == 'Filé Duplo' or tipoCarne == 'filé duplo' or tipoCarne == 'FILÉ DUPLO':
        tipoCarne = 'Filé Duplo'
        quantidade = float(
            input('Quantos quilos de carne?\n').replace(',', '.'))
        if quantidade <= 5:
            preço = 4.9
            total = (preço * quantidade)
        elif quantidade > 5:
            preço = 5.8
            total = (preço * quantidade)

        pagamento = input(
            'O pagamento é em dinheiro(D), cartão tabajara(CT) ou outro cartão(C)?\n')
        if pagamento == 'CT' or pagamento == 'ct' or pagamento == 'Cartão Tabajara' or pagamento == 'cartão tabajara' or pagamento == 'CARTÃO TABAJARA':
            pagamento = 'Cartão Tabajara'
            desconto = total * 0.05
            totalcdesc = total * 0.95
            print('\nTipo de carne: %s\nQuantidade: %sKg\nPreço total: R$%s\nTipo de pagamento: %s\nValor do desconto: R$%s\nTotal a pagar: R$%s\n' %
                  (tipoCarne, quantidade, total, pagamento, round(desconto, 2), round(totalcdesc, 2)))
        elif pagamento == 'C' or pagamento == 'c' or pagamento == 'Cartão'or pagamento == 'cartão' or pagamento == 'CARTÃO':
            pagamento = 'Outro cartão'
            desconto = 0
            totalcdesc = total
            print('\nTipo de carne: %s\nQuantidade: %sKg\nPreço total: R$%s\nTipo de pagamento: %s\nValor do desconto: R$%s\nTotal a pagar: R$%s\n' %
                  (tipoCarne, quantidade, total, pagamento, round(desconto, 2), round(totalcdesc, 2)))
        elif pagamento == 'D' or pagamento == 'd' or pagamento == 'Dinheiro' or pagamento == 'dinheiro' or pagamento == 'DINHEIRO':
            pagamento = 'Dinheiro'
            desconto = 0
            totalcdesc = total
            print('\nTipo de carne: %s\nQuantidade: %sKg\nPreço total: R$%s\nTipo de pagamento: %s\nValor do desconto: R$%s\nTotal a pagar: R$%s\n' %
                  (tipoCarne, quantidade, total, pagamento, round(desconto, 2), round(totalcdesc, 2)))
        else:
            print('Forma de pagamento inválida, tente outra!')

    elif tipoCarne == 'a' or tipoCarne == 'A' or tipoCarne == 'Alcatra' or tipoCarne == 'alcatra' or tipoCarne == 'ALCATRA':
        tipoCarne = 'Alcatra'
        quantidade = float(
            input('Quantos quilos de carne?\n').replace(',', '.'))
        if quantidade <= 5:
            preço = 5.9
            total = (preço * quantidade)
        elif quantidade > 5:
            preço = 6.8
            total = (preço * quantidade)

        pagamento = input(
            'O pagamento é em dinheiro(D), cartão tabajara(CT) ou outro cartão(C)?\n')
        if pagamento == 'CT' or pagamento == 'ct' or pagamento == 'Cartão Tabajara' or pagamento == 'cartão tabajara' or pagamento == 'CARTÃO TABAJARA':
            pagamento = 'Cartão Tabajara'
            desconto = total * 0.05
            totalcdesc = total * 0.95
            print('\nTipo de carne: %s\nQuantidade: %sKg\nPreço total: R$%s\nTipo de pagamento: %s\nValor do desconto: R$%s\nTotal a pagar: R$%s\n' %
                  (tipoCarne, quantidade, total, pagamento, round(desconto, 2), round(totalcdesc, 2)))
        elif pagamento == 'C' or pagamento == 'c' or pagamento == 'Cartão' or pagamento == 'cartão' or pagamento == 'CARTÃO':
            pagamento = 'Outro cartão'
            desconto = 0
            totalcdesc = total
            print('\nTipo de carne: %s\nQuantidade: %sKg\nPreço total: R$%s\nTipo de pagamento: %s\nValor do desconto: R$%s\nTotal a pagar: R$%s\n' %
                  (tipoCarne, quantidade, total, pagamento, round(desconto, 2), round(totalcdesc, 2)))
        elif pagamento == 'D' or pagamento == 'd' or pagamento == 'Dinheiro' or pagamento == 'dinheiro' or pagamento == 'DINHEIRO':
            pagamento = 'Dinheiro'
            desconto = 0
            totalcdesc = total
            print('\nTipo de carne: %s\nQuantidade: %sKg\nPreço total: R$%s\nTipo de pagamento: %s\nValor do desconto: R$%s\nTotal a pagar: R$%s\n' %
                  (tipoCarne, quantidade, total, pagamento, round(desconto, 2), round(totalcdesc, 2)))
        else:
            print('Forma de pagamento inválida, tente outra!')

    elif tipoCarne == 'p' or tipoCarne == 'P' or tipoCarne == 'Picanha' or tipoCarne == 'picanha' or tipoCarne == 'PICANHA':
        tipoCarne = 'Picanha'
        quantidade = float(
            input('Quantos quilos de carne?\n').replace(',', '.'))
        if quantidade <= 5:
            preço = 6.9
            total = (preço * quantidade)
        elif quantidade > 5:
            preço = 7.8
            total = (preço * quantidade)

        pagamento = input(
            'O pagamento é em dinheiro(D), cartão tabajara(CT) ou outro cartão(C)?\n')
        if pagamento == 'CT' or pagamento == 'ct' or pagamento == 'Cartão Tabajara' or pagamento == 'cartão tabajara' or pagamento == 'CARTÃO TABAJARA':
            pagamento = 'Cartão Tabajara'
            desconto = total * 0.05
            totalcdesc = total * 0.95
            print('\nTipo de carne: %s\nQuantidade: %sKg\nPreço total: R$%s\nTipo de pagamento: %s\nValor do desconto: R$%s\nTotal a pagar: R$%s\n' %
                  (tipoCarne, quantidade, total, pagamento, round(desconto, 2), round(totalcdesc, 2)))
        elif pagamento == 'C' or pagamento == 'c' or pagamento == 'Cartão' or pagamento == 'cartão' or pagamento == 'CARTÃO':
            pagamento = 'Outro cartão'
            desconto = 0
            totalcdesc = total
            print('\nTipo de carne: %s\nQuantidade: %sKg\nPreço total: R$%s\nTipo de pagamento: %s\nValor do desconto: R$%s\nTotal a pagar: R$%s\n' %
                  (tipoCarne, quantidade, total, pagamento, round(desconto, 2), round(totalcdesc, 2)))
        elif pagamento == 'D' or pagamento == 'd' or pagamento == 'Dinheiro' or pagamento == 'dinheiro' or pagamento == 'DINHEIRO':
            pagamento = 'Dinheiro'
            desconto = 0
            totalcdesc = total
            print('\nTipo de carne: %s\nQuantidade: %sKg\nPreço total: R$%s\nTipo de pagamento: %s\nValor do desconto: R$%s\nTotal a pagar: R$%s\n' %
                  (tipoCarne, quantidade, total, pagamento, round(desconto, 2), round(totalcdesc, 2)))
        else:
            print('Forma de pagamento inválida, tente outra!')

    else:
        print('Tipo inválido, tente outro')

    print('\nPressione qualquer tecla para continuar ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
