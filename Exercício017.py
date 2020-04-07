# 1- Se o ano for divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
# 2- Se o ano for divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
# 3- Se o ano for divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
# 4- O ano é um ano bissexto (tem 366 dias).
# 5- O ano não é um ano bissexto (tem 365 dias).
import msvcrt
while True:
    ano = int(input('Digite um ano para saber se ele é bissexto:\n'))

    if ano % 4 == 0 and ano % 100 != 0:
        print('O ano %s é bissexto, portanto tem 366 dias.' % ano)
    elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
        print('O ano %s é bissexto, portanto tem 366 dias.' % ano)
    else:
        print('O ano %s não é bissexto, portanto tem 365 dias.' % ano)

    print('\nPressione qualquer tecla para repetir ou pressione 1 para sair\n')
    command = msvcrt.getch()
    if command == b'1':
        break
