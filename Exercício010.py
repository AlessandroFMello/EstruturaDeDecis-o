turno = str.upper(input('Qual turno você estuda?\n'))

if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Turno inválido, tente novamente!')
input()
