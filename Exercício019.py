import msvcrt

while True:
    numero = int(input('Digite um número entre 1 e 999:\n'))

    unidade = numero % 10
    dezena = int(((numero - unidade)/10) % 10)
    centena = int(((numero - unidade)-dezena)/100)

    if unidade == 1 and dezena == 1 and centena == 1:
        print('\nO número %s tem: %s centena, %s dezena, %s unidade' %
              (numero, centena, dezena, unidade))

    elif unidade == 1 and dezena == 1:
        print('\nO número %s tem: %s centenas, %s dezena, %s unidade' %
              (numero, centena, dezena, unidade))

    elif dezena == 1 and centena == 1:
        print('\nO número %s tem: %s centena, %s dezena, %s unidades' %
              (numero, centena, dezena, unidade))

    elif unidade == 1 and centena == 1:
        print('\nO número %s tem: %s centena, %s dezenas, %s unidade' %
              (numero, centena, dezena, unidade))

    elif unidade == 1:
        print('\nO número %s tem: %s centenas, %s dezenas, %s unidade' %
              (numero, centena, dezena, unidade))

    elif dezena == 1:
        print('\nO número %s tem: %s centenas, %s dezena, %s unidades' %
              (numero, centena, dezena, unidade))

    elif centena == 1:
        print('\nO número %s tem: %s centena, %s dezenas, %s unidades' %
              (numero, centena, dezena, unidade))

    else:
        print('\nO número %s tem: %s centenas, %s dezenas, %s unidades' %
              (numero, centena, dezena, unidade))

    print('\nPressione qualquer tecla para continuar ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
