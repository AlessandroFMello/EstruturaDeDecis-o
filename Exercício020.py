import msvcrt

while True:
    aluno = str(input('Digite o nome do aluno:\n'))
    nota1 = float(input('Digite a nota G1 do aluno %s:\n' %
                        aluno).replace(',', '.'))
    nota2 = float(input('Digite a nota G2 do aluno %s:\n' %
                        aluno).replace(',', '.'))
    nota3 = float(input('Digite a nota G3 do aluno %s:\n' %
                        aluno).replace(',', '.'))

    media = (nota1 + nota2 + nota3)/3

    if media == 10:
        print('O aluno %s foi APROVADO COM DISTINÇÃO! Sua média é %s' %
              (aluno, round(media, 1)))

    elif media >= 7:
        print('O aluno %s foi APROVADO! Sua média é %s' %
              (aluno, round(media, 1)))
    else:
        print('O aluno %s foi REPROVADO! Sua média é %s' %
              (aluno, round(media, 1)))

    print('\nPressione qualquer tecla para continuar ou pressione 1 para sair')
    key = msvcrt.getch()
    if key == b'1':
        break
