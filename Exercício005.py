aluno = str(input('Digite o nome do aluno: \n'))
nota1 = float(input('Digite a nota da G1: \n'))
nota2 = float(input('Digite a nota da G2: \n'))
total = float(nota1 + nota2)/2

if total == 10:
    print('O aluno', aluno, 'foi APROVADO COM DISTINÇÃO! Nota:', total)
elif total >= 7:
    print('O aluno', aluno, 'foi APROVADO! Sua nota é:', total)
else:
    print('O aluno', aluno, 'foi REPROVADO! Sua nota é:', total)
input()
