import msvcrt

while True:
    print('Responda com sim(s) ou não(n)')

    total = 0

    condição = False
    while True:
        perg1 = input('Telefonou para a vítima?\n')
        if perg1 == 'SIM' or perg1 == 'Sim' or perg1 == 'sim' or perg1 == 'S' or perg1 == 's' or perg1 == 'Não' or perg1 == 'não' or perg1 == 'NÃO' or perg1 == 'N' or perg1 == 'n':
            total += 1
            perg1 = condição
            break
        elif perg1 == 'Não' or perg1 == 'não' or perg1 == 'NÃO' or perg1 == 'N' or perg1 == 'n':
            perg1 = condição
            break
        else:
            print('Resposta 1 inválida, tente novamente')
            True

    while True:
        perg2 = input('Esteve no local do crime?\n')
        if perg2 == 'SIM' or perg2 == 'Sim' or perg2 == 'sim' or perg2 == 'S' or perg2 == 's':
            total += 1
            perg2 = condição
            break
        elif perg2 == 'Não' or perg2 == 'não' or perg2 == 'NÃO' or perg2 == 'N' or perg2 == 'n':
            perg2 = condição
            break
        else:
            print('Resposta 2 inválida, tente novamente')
            True

    while True:
        perg3 = input('Mora perto da vítima?\n')
        if perg3 == 'SIM' or perg3 == 'Sim' or perg3 == 'sim' or perg3 == 'S' or perg3 == 's':
            total += 1
            perg3 = condição
            break
        elif perg3 == 'Não' or perg3 == 'não' or perg3 == 'NÃO' or perg3 == 'N' or perg3 == 'n':
            perg3 = condição
            break
        else:
            print('Resposta 3 inválida, tente novamente')
            True

    while True:
        perg4 = input('Devia para a vítima?\n')
        if perg4 == 'SIM' or perg4 == 'Sim' or perg4 == 'sim' or perg4 == 'S' or perg4 == 's':
            total += 1
            perg4 = condição
            break
        elif perg4 == 'Não' or perg4 == 'não' or perg4 == 'NÃO' or perg4 == 'N' or perg4 == 'n':
            perg4 = condição
            break
        else:
            print('Resposta 4 inválida, tente novamente')
            True

    while True:
        perg5 = input('Já trabalhou com a vítima?\n')
        if perg5 == 'SIM' or perg5 == 'Sim' or perg5 == 'sim' or perg5 == 'S' or perg5 == 's':
            total += 1
            perg5 = condição
            break
        elif perg5 == 'Não' or perg5 == 'não' or perg5 == 'NÃO' or perg5 == 'N' or perg5 == 'n':
            perg5 = condição
            break
        else:
            print('Resposta 5 inválida, tente novamente')
            True

    print('\nTotal: %s pontos' % total)

    if total <= 1:
        print('Inocente')
    elif total == 2:
        print('Suspeita')
    elif total >= 3 and total <= 4:
        print('Cúmplice')
    elif total == 5:
        print('Assassino')

    print('\nPressione qualquer tecla para continuar ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
