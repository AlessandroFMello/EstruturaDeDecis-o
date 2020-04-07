import msvcrt

while True:
    dia = int(input('Digite o dia:\n'))
    mes = int(input('Digite o mês:\n'))
    ano = int(input('Digite o ano:\n'))

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >= 1 and dia <= 31:
            print('\n%s / %s / %s' % (dia, mes, ano))
            print('Data válida!')
        else:
            print('\n%s / %s / %s' % (dia, mes, ano))
            print('Data inválida!')

    elif mes == 2:
        if dia >= 1 and dia <= 28:
            print('\n%s / %s / %s' % (dia, mes, ano))
            print('Data válida!')
        elif dia == 29:
            if ano % 4 == 0 and ano % 100 != 0:
                print('\n%s / %s / %s' % (dia, mes, ano))
                print('Data válida!')
            elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
                print('\n%s / %s / %s' % (dia, mes, ano))
                print('Data válida!')
            else:
                print('\n%s / %s / %s' % (dia, mes, ano))
                print('Data inválida')
        else:
            print('\n%s / %s / %s' % (dia, mes, ano))
            print('Data inválida!')

    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            print('\n%s / %s / %s' % (dia, mes, ano))
            print('Data válida!')
        else:
            print('\n%s / %s / %s' % (dia, mes, ano))
            print('Data inválida!')
    elif mes > 12:
        print('\n%s / %s / %s' % (dia, mes, ano))
        print('Data inválida')

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair')
    keypress = msvcrt.getch()
    if keypress == b'1':
        break
