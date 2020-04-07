import msvcrt

while True:
    numero1 = float(input('Digite um número:\n').replace(',', '.'))
    numero2 = float(input('Digite outro número:\n').replace(',', '.'))

    soma = numero1 + numero2
    subtração = numero1 - numero2
    multiplicação = numero1 * numero2
    divisão = numero1 / numero2

    operação = input(
        'Qual operação matemática você deseja realizar (soma, subtração, multiplicação, divisão)?\n')
    if operação == 'soma' or operação == 'Soma' or operação == 'SOMA' or operação == '+':
        operação = soma
        OP = 'soma'
    elif operação == 'subtração' or operação == 'Subtração' or operação == 'SUBTRAÇÃO' or operação == '-':
        operação == subtração
        OP = 'subtração'
    elif operação == 'multiplicação' or operação == 'Multiplicação' or operação == 'MULTIPLICAÇÃO' or operação == '*':
        operação = multiplicação
        OP = 'multiplicação'
    elif operação == 'divisão' or operação == 'Divisão' or operação == 'DIVISÃO' or operação == '/':
        operação = divisão
        OP = 'divisão'
    else:
        print('Operação inválida, tente novamente!')

    print('\nA %s entre %s e %s é igual a: %s' %
          (OP, numero1, numero2, operação))
    print('O número %s é:' % operação)

    if operação == 0:
        print('Zero não é par nem ímpar')
    elif operação % 2 == 0:
        print('PAR')
    else:
        print('ÍMPAR')

    if operação > 0:
        print('POSITIVO')
    elif operação < 0:
        print('NEGATIVO')

    if operação // 1 == operação:
        print('INTEIRO')
    else:
        print('DECIMAL')

    print('\nPressione qualquer tecla para continuar ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
