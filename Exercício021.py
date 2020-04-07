import msvcrt

while True:
    saque = int(input('Digite o valor a ser sacado:\n'))
    if saque > 600 or saque < 10:
        print('Valor inválido!')
        print('É possivel sacar entre 10 e 600 reais')
        print('Tente novamente')

    else:
        print('Valor do saque: R$%s' % saque)

        notasdecem = int(saque/100)
        saque = saque % 100
        notasdecinq = int(saque/50)
        saque = saque % 50
        notasdedez = int(saque/10)
        saque = saque % 10
        notasdecinc = int(saque/5)
        saque = saque % 5
        notasdeum = saque

        print('Notas de 100 = %s\nNotas de 50 = %s\nNotas de 10 = %s\nNotas de 5 = %s\nNotas de 1 = %s\n' %
              (notasdecem, notasdecinq, notasdedez, notasdecinc, notasdeum))

    print('\nPressione qualquer tecla para continuar ou pressione 1 para sair')
    command = msvcrt.getch()
    if command == b'1':
        break
